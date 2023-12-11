package 상속.Super;

public class ColorPoint extends Point{

    private String color;
    


    public ColorPoint(int x, int y, String color){
        super(x,y);
        this.color = color;
    }

    public void showPoint(){
        System.out.print("이게 다형성이야 !!!!!!!");
    }
    public void showColorPoint(){
        System.out.print(color);
        showPoint();
    }
}
