package 참조타입;

import java.util.Scanner;

public class MaxNumber {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int intArray[] = new int[5];
        
        int max=0;
        System.out.println("양수 5개를 입력해라.");

        for(int i=0;i<5;i++){
            intArray[i] = scanner.nextInt();
            if(intArray[i]>max){
                max=intArray[i];
            }
        }
        System.out.println(max);
        scanner.close();
        // int max=0;
    }
}