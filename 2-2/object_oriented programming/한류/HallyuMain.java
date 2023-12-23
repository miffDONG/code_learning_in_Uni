import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

import java.io.File;
import java.text.SimpleDateFormat;

import inheritancePart.*;
import interfacePart.*;

public class HallyuMain {
    public static void main(String[] args) {

        int in[]= new int[10];
        in[1] = ((int) Math.random()*10);
        // 배열
        // 시기별 콘텐츠 및 점유율. 단위 %
        Double[] K_POP = { 14.9, 12.3, 12.0, 17.2, 20.1, 12.1, 16.6, 17.3, 18.5, 16.8 };
        Double[] Drama = { 18.3, 12.9, 8.4, 9.9, 9.5, 9.9, 7.6, 6.8, 7.8, 6.4 };
        Double[] KoreanFood = { 14.5, 15.8, 10.7, 10.5, 12.1, 12.5, 7.5, 9.9, 12.2, 12.0 };

        // List 컬렉션
        // 조사한 시기 데이터. 순서대로 1차~10차까지.
        List<String> list = new ArrayList<String>();
        list.add("2012.02"); //1차
        list.add("2012.12"); //2차
        list.add("2014.02");
        list.add("2014.11");
        list.add("2015.11");
        list.add("2016.11");
        list.add("2017.11");
        list.add("2018.11");
        list.add("2019.11");
        list.add("2020.10"); //10차



        // 서비스 진행 순서
        // 1. 기능 선택
        // 2. 기능 수행

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("시기에 따른 순위 조회 : 1");
            System.out.println("한류 콘텐츠 점유율 변화 조회 : 2");
            System.out.println("순위 조회 : 3");
            
            //1. 기능 선택
            int Func = scanner.nextInt();
            
            // 2. 기능수행
            // 2-1. 순위 조회.
            // 입력 : 차수
            // 출력 : 1위 - 2위 - 3위
            // 배열, 상속
            if (Func == 1) {
                System.out.println("차수를 입력하시오 {1차(2014년 2월) ~ 10차(2020년 10월)}");
                int surveyDate = scanner.nextInt();
                surveyDate--;
                System.out.println(list.get(surveyDate) + "순위 조회를 시작합니다.");
                Ranking ranking = new Ranking();
                ranking.check(K_POP[surveyDate], Drama[surveyDate], KoreanFood[surveyDate]);
            }

            // 2-2. 컨텐츠 점유율 변화 조회
            // 입력 : 컨텐츠
            // 출력 : 차수별 컨텐츠
            // 열거타입, 상속
            if (Func == 2) {
                System.out.println("한류 컨텐츠를 선택하시오");
                System.out.println("K-pop : 1");
                System.out.println("Drama : 2");
                System.out.println("Korean Food : 3");

                HallyuKind cont = null;
                MarketShare marketShare = new MarketShare();
                int content = scanner.nextInt();

                switch (content) {
                    case 1:
                        cont = HallyuKind.K_POP;
                        System.out.println(cont);
                        marketShare.check(K_POP, list);
                        break;
                    case 2:
                        cont = HallyuKind.Drama;
                        System.out.println(cont);
                        marketShare.check(Drama, list);
                        break;
                    case 3:
                        cont = HallyuKind.KoreanFood;
                        System.out.println(cont);
                        marketShare.check(KoreanFood, list);
                        break;
                }

            }

            // 2-3. 해당년도 순위 조회
            // 입력 : 등수 , 년도
            // 출력 : 컨텐츠
            // 인터페이스
            if (Func == 3) {
                System.out.println("원하는 등수를 입력하시오 (1~3)");
                int n = scanner.nextInt();
                if (n == 1) {
                    FirstPrint firstPrint = new FirstPrint();
                    firstPrint.funcStart();
                    int ye = scanner.nextInt();
                    String year = String.valueOf(ye);

                    for (int i = 0; i < list.size(); i++) {
                        if (list.get(i).contains(year)) {
                            firstPrint.Pr(K_POP[i], Drama[i], KoreanFood[i], list.get(i));
                        }
                    }
                }
                if (n == 2) {
                    SecondPrint secondPrint = new SecondPrint();
                    secondPrint.funcStart();
                    int ye = scanner.nextInt();
                    String year = String.valueOf(ye);

                    for (int i = 0; i < list.size(); i++) {
                        if (list.get(i).contains(year)) {
                            secondPrint.Pr(K_POP[i], Drama[i], KoreanFood[i], list.get(i));
                        }
                    }
                }
                if (n == 3) {
                    ThirdPrint thirdPrint = new ThirdPrint();
                    thirdPrint.funcStart();
                    int ye = scanner.nextInt();
                    String year = String.valueOf(ye);

                    for (int i = 0; i < list.size(); i++) {
                        if (list.get(i).contains(year)) {
                            thirdPrint.Pr(K_POP[i], Drama[i], KoreanFood[i], list.get(i));
                        }
                    }
                }
            }


            //서비스 종료 후 이 서비스를 구성하는 파일 열람 가능. 파일 출력.
            System.out.println("파일 구성을 열람하시겠습니까?");
            System.out.println("예 : 0 , 아니오 : 1");
            int ch = scanner.nextInt();

            if (ch == 0) {
                File files = new File("C:/Users/hyundong/Desktop/한류");
                File[] contents = files.listFiles();
                System.out.println("");
                System.out.println("----------------한류 처리 프로그램 폴더 및 파일----------------");
                System.out.println("시간\t\t\t형태\t\t크기\t이름");
                System.out.println("---------------------------------------------------------------");
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd a HH:mm");
                for (File file : contents) {
                    System.out.print(sdf.format(new Date(file.lastModified())));
                    if (file.isDirectory()) {
                        System.out.println("\t<DIR>\t\t\t" + file.getName());
                    } else {
                        System.out.println("\t\t\t" + file.length() + "\t" + file.getName());
                    }
                }

            } else {
                System.out.println("서비스를 종료합니다.");
            }

        //예외처리.
        //정수가 아닌 입력이 들어왔을 때, 서비스를 종료하며 정수 입력을 유도하는 문구 출력.    
        }catch (Exception e) {
            System.out.println("정수를 입력하세요.");
        }

    }

}
