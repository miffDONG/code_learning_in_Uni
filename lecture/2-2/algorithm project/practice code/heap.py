class Heap:
    def __init__(self,L=[]):
        self.A=L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def make_heap(self):
        n=len(self.A)
        for k in range(n-1,-1,-1):
            self.heapify_down(k,n)

    def heapify_down(self, k, n): #작은 값을 아래로
        while 2*k+1 < n:  #자식노드가 있는가?
            L,R = 2*k+1,2*k+2            #L 왼쪽 자식노드, 우측 자식노드
            if L<n and self.A[L] > self.A[k]: #부모노드와 비교
                m=L
            else:
                m=k
            if R<n and self.A[R]> self.A[m]:
                m=R  #우측 좌측 자식노드를 부모노드와 비교 끝
            if m!=k: #m = max 아니면 교환
                self.A[k], self.A[m] = self.A[m],self.A[k]
                k=m
            else: break

    def heap_sort(self):
        n=len(self.A)
        for k in range(len(self.A)-1,-1,-1):
            self.A[0],self.A[k]=self.A[k],self.A[0]
            n=n-1
            self.heapify_down(0,n)

A=Heap([6,5,4,37,8,1,34,13,631,72,345,143,1324,3,2436,3,1324,125,3123,412,35,324,6,23,62,436])
print(A.heap_sort())
print(A)