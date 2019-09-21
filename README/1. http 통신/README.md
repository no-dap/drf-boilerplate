# HTTP 통신

## 특징  
1. http는 기본적으로 1회요청 - 1회 응답을 기본으로 합니다.
2. stateless
- 각 HTTP 통신은 독립적이며 그 전에 처리된 HTTP 통신에 대해 전혀 알 수 없습니다.  
- 요청자의 상태를 저장할 필요가 없으므로 HTTP 통신 간의 진행이나 연결 상태의 처리, 저장을 구현 및 관리하지 않습니다.  

## 구조
request, response 모두  
- start line  
- header  
- body  
의 구조로 되어있습니다. 
  
header의 경우 drf에서 request.META, body의 경우 request.data로 전달되므로 직접 살펴봅시다.  
request header에 가장 자주 추가해주는 정보는 authorization 입니다.  
보통 drf를 사용하면 Token Authorization을 주로 사용합니다.  
(Session Authorization의 경우 http의 stateless를 위배하기 때문에 별로 좋아하지 않습니다)  
header에는 다음같은 모양으로 들어갑니다.  
'Authorization': 'Token {token value}'  
웹개발이 주 목적이므로 contents type은 당연히 application/JSON 방식이 가장 유용합니다.  
(JSON == JavaScript Object Notation이므로 큰 변조 없이 바로 사용 가능)  
  
request에 data가 필요한 경우 POST, PUT, PATCH의 경우 body에 심어서 보내면 되지만  
GET의 경우 body를 보내지 않는것이 convention입니다.  
따라서 이 경우에는 query parameter를 이용합니다. (다른 method에서도 사용 가능)  
다만 url이 intercept당하기 가장 쉬우므로 민감한 정보는 url에 넣는 것을 지양해야합니다.  
