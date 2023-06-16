#include <stdio.h>
#include <stdlib.h>

// 제약조건
// 1. input 으로 주어지는 파일의 한줄은 100자를 넘지 않음.
// 2. input 으로 주어지는 파일의 길이는 100000줄을 넘지 않음. 즉, address trace 길이는 100000줄을 넘지 않음.
#define MAX_ROW     100000
#define MAX_COL     2
#define MAX_INPUT   100

// 구현해야하는 함수
void solution(int cache_size, int block_size, int assoc);
void read_op(int addr, int cache_size, int block_size, int assoc);
void write_op(int addr, int cache_size, int block_size, int assoc);
void fetch_inst(int addr, int cache_size, int block_size, int assoc);
int evict(int set, int assoc, char mode);
// 전역변수
// 문제를 풀기 위한 힌트로써 제공된 것이며, 마음대로 변환 가능합니다.
enum COLS {
    MODE,
    ADDR
};

struct i_cache {
    int tag;
    int valid;
    int time;
};

struct d_cache {
    int tag;
    int valid;
    int time;
    int dirty;
};


int i_total, i_miss;            /* instructino cache 총 접근 횟수, miss 횟수*/
int d_total, d_miss, d_write;   /* data cache 접근 횟수 및 miss 횟수, memory write 횟수 */
int trace[MAX_ROW][MAX_COL] = { {0,0}, };
int trace_length = 0;

int time_count;

struct i_cache* ip;
struct d_cache* dp;

int main() {
    // DO NOT MODIFY -- START --  //
    // cache size
    int cache[5] = { 1024, 2048, 4096, 8192, 16384 };
    // block size
    int block[2] = { 16, 64 };
    // associatvity e.g., 1-way, 2-way, ... , 8-way
    int associative[4] = { 1, 2, 4, 8 };
    int i = 0, j = 0, k = 0;

    /* 입력 받아오기 */
    char input[MAX_INPUT];
    while (fgets(input, sizeof(input), stdin)) {
        if (sscanf(input, "%d %x\n", &trace[trace_length][MODE], &trace[trace_length][ADDR]) != 2) {
            fprintf(stderr, "error!\n");
        }
        trace_length++;
    }


    /* 캐시 시뮬레이션 */
    printf("cache size || block size || associative || d-miss rate || i-miss rate || mem write\n");
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 2; j++) {
            for (k = 0; k < 4; k++) {
                solution(cache[i], block[j], associative[k]);
            }
        }
    }
    // DO NOT MODIFY -- END --  //

    return 0;
}

void solution(int cache_size, int block_size, int assoc) {

    i_total = i_miss = 0;
    d_total = d_miss = d_write = 0;

    int num = cache_size / block_size;
    ip = (struct i_cache*)calloc(num, sizeof(struct i_cache));
    dp = (struct d_cache*)calloc(num, sizeof(struct d_cache));

    // DO NOT MODIFY -- START --  //
    int mode, addr;
    double i_miss_rate, d_miss_rate;    /* miss rate을 저장하는 변수 */

    int index = 0;
    while (index != trace_length) {
        mode = trace[index][MODE];
        addr = trace[index][ADDR];

        switch (mode) {
        case 0:
            read_op(addr, cache_size, block_size, assoc);
            d_total++;
            break;
        case 1:
            write_op(addr, cache_size, block_size, assoc);
            d_total++;
            break;
        case 2:
            fetch_inst(addr, cache_size, block_size, assoc);
            i_total++;
            break;
        }
        index++;
    }
    // DO NOT MODIFY -- END --  //

    // hint. data cache miss rate 와 intruction cache miss rate를 계산하시오. 
    // ? 에는 알맞는 변수를 넣으면 됩니다. addr[i]에 data[k]가 있는지 확인. 

    i_miss_rate = (double)i_miss / i_total;
    d_miss_rate = (double)d_miss / d_total;


    // DO NOT MODIFY -- START --  //
    printf("%8d\t%8d\t%8d\t%.4lf\t%.4lf\t%8d\n", cache_size, block_size, assoc, d_miss_rate, i_miss_rate, d_write);
    // DO NOT MODIFY -- END --  //
}

// 아래 함수를 직접 구현하시오, 차례로 읽기, 쓰기, 그리고 인스트럭션 fetch 동작입니다.



void read_op(int addr, int cache_size, int block_size, int assoc) {
    int i, ev_index = 0;
    int setNum = cache_size / (assoc * block_size);
    int set = (addr / block_size) % setNum;
    struct d_cache* p;
    int hit = 0;

    for (i = 0; i < assoc; i++) {
        p = &dp[set * assoc + i];

        if (p->valid == 1 && p->tag == addr / (block_size * setNum)) {
            p->time = time_count++;
            hit++;
            return;
        }

    }

    if (hit == 0) {
        d_miss++;
        ev_index = evict(set, assoc, 'd');
        p = &dp[set * assoc + ev_index];
        if (p->dirty == 1 && p->valid == 1)
            d_write++;

        p->valid = 1;
        p->time = time_count++;
        p->tag = addr / (block_size * setNum);
        p->dirty = 0;
    }

    return;
}


void write_op(int addr, int cache_size, int block_size, int assoc) {
    int i, ev_index = 0;
    int setNum = cache_size / (assoc * block_size);
    int set = (addr / block_size) % setNum;
    struct d_cache* p;
    int hit = 0;

    for (i = 0; i < assoc; i++) {
        p = &dp[set * assoc + i];

        if (p->valid == 1 && p->tag == addr / (block_size * setNum)) {
            hit = 1;
            p->time = time_count++;
            p->dirty = 1;
            return;
        }

    }

    if (hit == 0) {
        d_miss++;
        ev_index = evict(set, assoc, 'd');
        p = &dp[set * assoc + ev_index];

        if (p->dirty == 1 && p->valid == 1)
            d_write++;

        p->valid = 1;
        p->time = time_count++;
        p->tag = addr / (block_size * setNum);
        p->dirty = 1;
    }

    return;
}

void fetch_inst(int addr, int cache_size, int block_size, int assoc) {
    int i, ev_index = 0;
    int setNum = cache_size / (assoc * block_size);
    int set = (addr / block_size) % setNum;
    struct i_cache* p;
    int hit = 0;

    for (i = 0; i < assoc; i++) {
        p = &ip[set * assoc + i];
        if (p->valid == 1 && p->tag == addr / (block_size * setNum)) {
            hit++;
            p->time = time_count++;
            return;
        }
    }

    if (hit==0) {
        i_miss++;
        ev_index = evict(set, assoc, 'i');
        p = &ip[set * assoc + ev_index];

        p->valid = 1;
        p->time = time_count++;
        p->tag = addr / (block_size * setNum);

    }
    return;
}

int evict(int set, int assoc, char mode) {
    int i, tmp_time = 0;
    int min = time_count + 1, min_i = 0;

    for (i = 0; i < assoc; i++) {
        if (mode == 'd')
            tmp_time = dp[set * assoc + i].time;
        else if (mode == 'i')
            tmp_time = ip[set * assoc + i].time;

        if (min > tmp_time) {
            min = tmp_time;
            min_i = i;
        }
    }

    return min_i;
}
// hint. LRU 알고리즘 교체 정책을 구현하기 위한 함수도 작성하셔서 적용하면 됩니다.


