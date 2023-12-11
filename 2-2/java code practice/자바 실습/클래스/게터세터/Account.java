package 클래스.게터세터;

public class Account {
    private String name;
    private int Balance;
    
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public int getBalance(){
        return Balance;
    }
    public void setBalance(int Balance){
        if(Balance>0){
            this.Balance = Balance;
        }
        else{
            this.Balance = 0;
            return;
        }
    }
}
