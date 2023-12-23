package inheritancePart;

public class Ranking extends Function{
 
    //start 메소드 오버라이딩. 순위 조회 서비스를 알리는 문구 출력.
    @Override
    void start(){System.out.println("시기에 따른 순위 조회입니다.");}

    
    //조사한 데이터 차수 1차~10차 중 한 차수를 정렬.
    //1위 ~ 3위 컨텐츠 출력
    public void check(Double K_POP, Double Drama, Double KoreanFood){

        Double[] list = {K_POP,Drama,KoreanFood};
        String[] listContents = {"K_POP","Drama","KoreanFood"};
        for(int i=0; i<3;i++){
            for(int j=i+1; j<3; j++){
                if(list[i]<list[j]){
                    Double tmp = list[i];
                    list[i] = list[j];
                    list[j] = tmp;

                    String tmp2 = listContents[i];
                    listContents[i] = listContents[j];
                    listContents[j] = tmp2;
                }
            }
        }

        System.out.println("1위 : "+listContents[0]+" '"+list[0]+"%'");
        System.out.println("2위 : "+listContents[1]+" '"+list[1]+"%'");
        System.out.println("3위 : "+listContents[2]+" '"+list[2]+"%'");
    }

}