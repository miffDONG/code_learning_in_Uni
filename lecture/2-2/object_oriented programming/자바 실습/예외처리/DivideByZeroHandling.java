package 예외처리;

import java.util.Scanner;

public class DivideByZeroHandling {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int dividend;
        int divisor;
        while(true){
            System.out.print("나뉨수를 입력하시오: ");
            dividend = scanner.nextInt();
            System.out.print("나눗수를 입력하시오: ");
            divisor = scanner.nextInt();

            try{
                System.out.println(dividend/divisor);
            }
            catch(ArithmeticException e){
                System.out.println("0은 안돼!");
            };
        }
    }
    
}
