# Docker

## Why?
Docker는 virtual machine을 생성해주는 tool입니다.  
사용하는 이유는 여러 가지가 있지만, server deployment에서 가장 중요한 사용 이유는  
enviroment를 똑같이 제공해서 어떤 machine에서도 일관성 있는 deploy를 하기 위함입니다.  

## Docker pull
Docker는 다른 image를 docker hub에서 pull 해와서 사용할 수 있습니다.  
따라서 매 deploy마다 환경을 설정해줄 필요 없이 미리 공통적으로 사용할만한 image를 생성하여  
docker hub에 push를 해둔 후, 필요할때마다 from을 통해 가져와서 사용합니다.  
[docker image push example link](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter13/02)

## Docker run
Docker를 사용하게 되면 VM이라는 하나의 layer가 추가되는 개념이므로,  
VM에서 돌고있는 웹서버(nginx)의 외부port와 실제 머신의 외부 port를 연결해주어야 합니다.  
Docker기 실행이 되면 Dockerfile에 지정해놓은 명령어 대로 supervisord를 실행하고,  
supervisord가 nginx와 uwsgi를 실행하게 됩니다.  

## TODO
1. base로 사용할 이미지 build후 push하기
2. 위에서 push한 이미지만 pull해서 수동으로 로컬에서 deploy해보기
3. Dockerfile을 완성해 자동으로 로컬에서 deploy해보기
