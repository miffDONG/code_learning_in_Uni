package 스레드.스레드상속;

import java.awt.Toolkit;
public class TestThread {
    public static void main(String[] args){
        Thread th = new TimerThread();
        th.start();

        Toolkit toolkit = Toolkit.getDefaultToolkit();
        while(true){
            toolkit.beep();
            try{
                Thread.sleep(100);
            }
            catch(Exception e){}
        }
    }
}
