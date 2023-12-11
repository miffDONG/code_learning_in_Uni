package 클래스.this사용;

public class Book {
    
    String title;
    String author;

    public Book(){
        this.title = "";
        this.author = "";
    }
    public Book(String title){
        this.title = title;
        this.author = "작자미상";
    }

    public Book(String title, String author){
        this.title = title;
        this.author = author;
    }

    void show(){
        System.out.println("제목 : " + title +", 작가 : " + author);
    }
}
