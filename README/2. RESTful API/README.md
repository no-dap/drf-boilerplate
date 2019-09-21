# RESTful API
인터넷에 여러가지 설명글들이 많이 있지만 단순히 api 설계 방법론이므로  
간단하게만 숙지하시면 됩니다.  
## 특징
1. url은 명사형, method가 동사  
url을 하나의 문장이라고 생각했을 때, 동사는 method가 담당합니다.
```
  GET /user/create-user/ (x)  
  POST /user/ (o)  
  
  POST /user/update-user/ (x)  
  PATCH /user/2/ (o)  
```
2. 계층구조는 / 로 구분  
```
  GET /question/answer/  
  클라이언트 개발자 입장에서 answer가 question에 종속되어 있다는 것을 바로 인지 가능  
  
  GET /question/1/answer/  
  마찬가지로 1번 question의 answer가 return되겠구나 라는 것을 추측 가능  
```
3. 적절한 status code return  
status code는 자주 사용하는 것이 몇 가지 있으므로 외워두시는게 좋습니다.  
### success  
	200 : ok
	201 : 생성됨
	204 : 보여줄 정보가 없음
	301 : 영구적으로 이동됨 (redirection)
	302 : 임시로 이동됨 (redirection)
### error  
	400 : 요청 데이터 포멧 오류
	401 : 인증되지 않은 요청
	403 : 권한 없음
	500 : 내부 서버 오류
	502 : gateway 오류
