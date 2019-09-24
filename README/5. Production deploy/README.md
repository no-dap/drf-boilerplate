# Production Deployment  

실제 production 서버는 dev환경과 완전히 분리되어야 하므로 다른 설정파일을 갖도록 세팅을 해주어야 합니다.  
분리되어야 하는 세팅은 아래와 같습니다.
  
- database
- file storage
- debug
- allowed host
- debugging service

## TODO
1. django settings 파일 구조 변경하기
2. production 환경으로 deploy 해보기
3. debugging service([sentry.io](https://sentry.io/))를 사용해 실제로 error reporting을 받아보기
