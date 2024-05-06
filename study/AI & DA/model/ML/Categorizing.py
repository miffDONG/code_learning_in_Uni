import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"Mary slapped the green witch.")
for token in doc:
	print('{}-->{}'.format(token,token.pos_))

for chunk in doc.noun_chunks:
	print('{}-->{}'.format(token,chunk.label_))

xgboost, LGBM

autoML test data만 써서 성능 확인. feature 중요도 확인

포트폴리오 피드백 페이지
개별 종목 평가 페이지

23-2 학기 피버스 개강총회가 9월 18일(월) 정규 활동 후에 열릴 예정입니다. 
이 자리는 신입부원과 기존부원 간에 친해질 수 있는 자리가 될 것입니다. 

장소는 결정되는 대로 공지하겠습니다.

❗23-2 피버스 개강총회❗

✅일시: 9월18일(월) 오후 9시 30분

✅ 장소: 추후 공지

✅ 참가비: 추후 공지   
* 참가 인원 보고 회비를 사용할지 결정.

다음주 월요일 정규활동 후 부원끼리 알아갈 수 있는 자리를 마련하고자 합니다.
참가를 희망하시는 분들은 투표해주세요!



