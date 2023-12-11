package 클래스.signletonExample;

public class Singleton {
    //정적 필드
    //single은 전체 프로그램에서 단 하나의 객체만 생성 가능
    //그래서 그런지 class 함수에서 만드네요
    private static Singleton singleton = new Singleton();

    //생성자
    private Singleton(){}

    //정적 필드. 
    //single을 불러오는 메소드
    static Singleton getInstance(){
        return singleton;
    }
}
