# AWS
AWS에는 다양한 서비스가 존재하지만, 주로 사용할만한 몇 가지중 설명이 필요한 것들을 정리했습니다.

## Lambda
Cloud computing을 통해 원하는 코드를 실행시켜주는 서비스입니다.  
invocation 횟수에 따라 과금되는 구조이며 기본적으로 외부로 computing을 요청하는 것이므로 asynchronous하게 이용할 수 있습니다.  
(사용량이 많을 경우 queue 고려)  
실행할 코드를 package로 만들어서 이름을 지정해 업로드하면 되며, python에서는 boto3를 통해 사용합니다. 
  
[boto3 lambda documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html)

## SES
Email 서비스입니다. django에서 마찬가지로 boto3를 통해 사용할 수 있습니다.

## Elastic beanstalk
서버 deploy를 위한 패키지 서비스입니다. 기본적으로 업로드하는 코드에서 알아서 deploy방식을 파싱하여 그에 맞는 환경을 제공합니다.  
생성할 EC2 instance 지정, 같은 VPC로 묶여있는 RDS생성 등을 한번에 실행할 수 있으며,  
enviroment variable의 지정이나 auto scaling 세팅, 각 EC2 instance에 ssh 접속등이 가능합니다.  

## Elastic Load Balancer
Auto scaling을 위해 존재하는 서비스로 beanstalk application을 deploy하면 자동적으로 생성됩니다.  
내부는 scaling 세팅을 받아서 실제로 실행하는 코드와 nginx로 구성되어 있습니다.  
3종류의 load balancer가 존재하는데, 일반적인 웹서버의 경우 classic type을 주로 사용합니다.  
  
[ELB 소개 페이지](https://aws.amazon.com/ko/elasticloadbalancing/)

## EB-CLI
AWS에서 제공하는 python package로 command line에서 각종 서비스를 컨트롤할 수 있습니다.
  
[awsebcli documentation](https://pypi.org/project/awsebcli/)

## TODO
1. boto3를 사용해서 사용중인 static storage를 S3로 옮겨보기
2. boto3를 사용해서 lambda invocation 해보기
3. eb-cli 세팅하기
4. deployment 세팅 이후 beanstalk을 통해 웹서버 deploy 해보기
5. auto scaling 세팅해보기
