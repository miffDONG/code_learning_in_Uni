package 참조타입;

public class Foreach {
    public static void main(String args[]){
        String names[] = {"사과","배","바나나","체리","딸기","포도"};

        int i =1;
        for(String s : names){
            System.out.print(i+"-"+s+" ");
            i++;
        }
    }
}
