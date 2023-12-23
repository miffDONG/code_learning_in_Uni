# PatentClassification - 5조
### 팀프로젝트
- 주제 : 특허 문서 기반 특허 분류

- 목표 : 문서의 text를 분석하여 적합한 분류 번호(SSno)를 출력하는 모델 생성

- 기술적 목표 : 전처리 및 적합한 모델 선정으로 특허 분류의 정확도 향상
  1. text 전처리 - 기호, 이미지 text, 영어, 한자 etc...
  2. model - `koelectra` , `KorPatELECTRA` 성능 비교
     * KorPatELECTRA는 한국특허정보원에서 국내특허문언 text를 pretraining 한 모델
---------------

## 파일 구조
```
data
├─  train
│   ├─  docs
│   └─  labels
├─  test
│   └─  test_input.csv
└─  sample_submission.csv

baseline
├─  config
│   └─  preprocess.yaml, train.yaml, pred.yaml
├─  modules
│   └─  loss.py
├─  preprocess.py, train.py, pred.py
├─  Readme.md
│ 
└─  results
    └─  checkpoint-#####
        └─  submission.csv
```
- config: 전처리/학습/추론 hyperparameter 설정
  - train.yaml
  - pred.yaml
  - preprocess.yaml

- preprocess.py: 전처리 코드. `train.csv`, `category.csv` 파일 생성
- train.py: 학습 코드. `./results/checkpoint-#####` , `runs` 생성
- predict.py: 추론 코드. `./results/checkpoint-#####/submission.csv` 생성

--------------------

## 하이퍼 파라미터
- train.yaml
  - lr_scheduler_type: `constant_with_warmup` or 'cosine_with_restarts`
  - learning_rate: 5e-5~8e-4
  - epoch: 10~100
  #### 실험 모니터링
  - report_to: ['tensorboard']
  - save_strategy: 'steps'
  - save_steps: 890
  - logging_steps: 89

![Untitled](https://github.com/miffDONG/PatentClassification/assets/100841549/57880cb2-8002-46dd-a3b6-b563cc30ea76)
  
- pred.yaml
  - threshold 1.5~2.0
