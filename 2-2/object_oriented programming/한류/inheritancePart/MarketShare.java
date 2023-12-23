package inheritancePart;

import java.util.List;

public class MarketShare extends Function{

    //start 메소드 오버라이딩. 시장 점유율 서비스를 알리는 문구 출력.
    @Override
    void start(){System.out.println("한류 콘텐츠 점유율 변화 조회입니다.");}

    //컨텐츠 하나의 점유율 기록들을 년도 별로 출력.
    public void check(Double[] content, List<String> list){
        for(int i = 0; i<content.length; i++){
            System.out.println(list.get(i)+" 점유율 "+content[i]+"%");
        }
    }


}
