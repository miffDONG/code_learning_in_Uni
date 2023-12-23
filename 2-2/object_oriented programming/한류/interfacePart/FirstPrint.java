package interfacePart;

public class FirstPrint implements Know{
    @Override
    public void funcStart(){
        System.out.println("1위를 알고싶은 년도를 선택하세요 2012~2020");
    }


    //해당 년도의 컨텐츠들을 하나씩 매개변수로 받아 정렬. 1순위를 출력.
    @Override
    public void Pr(Double K_POP, Double Drama, Double KoreanFood, String survey) {
        Double[] list = {K_POP,Drama,KoreanFood};
        String[] listContents = {"K_POP","Drama","KoreanFood"};

        System.out.println("***** "+survey+" 1위 조회 *****");
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

        System.out.println(listContents[0]);
    }
}
