package 참조타입;

public class DiceFrequency {
    public static void main(String args[]){
        final int SIZE = 6;
        int freq[] = new int[SIZE];
        
        for(int i = 0; i < 10000; i++){
            ++freq[(int)(Math.random() *SIZE)];
        }

        for(int i = 0; i<SIZE; i++){
            System.out.println(freq[i]);
        }
    }
}
