# Test
기본적으로 django, rest_framework 둘 다 testcode를 위한 server-side client를 지원합니다.  
test cycle은 실행할 때마다 비어있는 database 서버에 현재 작성되어 있는 migration을 모두 실행하고  
테스트 코드를 모두 실행한 후 database를 다시 destroy하는 것이 1회입니다.  
텅텅 비어있는 db에서 코드가 돌아가기 때문에 의존적인 데이터는 모두 세팅을 해주어야 합니다.  
test 명령어를 실행 시 test로 시작하는 모든 파이썬 파일 내부의 TestCase class 아래에 test_로 시작하는 모든 함수를 한번씩 실행합니다.  
우리가 개발할 것은 API서버이기 때문에, 사전에 client 개발자와 약속된 input을 받아  
적절한 output을 내는 지 검사하는 코드를 간단하게 작성하면 됩니다.

## Example
```
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


class FooAPITestCase(APITestCase):
	def setUp(self):
		"""
		TestCase class의 constructor입니다. setUp은 각 test code가 실행되기 전에 한번씩 실행됩니다.
		API test이므로 client등록은 거의 필수로 들어가 있으며,
		상기한 의존적인 데이터 생성 또한 여기서 하면 좋습니다.
		"""
		from .models import Bar, User
		self.client = APIClient()  # client 등록. 사용법은 하단 서술
		self.user = User.objects.create(**kwargs)  # 의존적인 데이터 미리 생성
		self.my_bar = Bar.objects.create(**kwargs)  # 의존적인 데이터 미리 생성
		token, _ = Token.objects.get_or_create(user=self.user)  # credential이 필요한 API test의 경우 token까지 생성
		self.token_key = token.key  # token key 가져오기
		self.client.credentials(Authorization=f'Token {self.token_key}')
		# 이제 client는 request마다 auth header가 포함됩니다.
		
	def test_get_foo(self):
		client = self.client
		url = '/api/v1/foo/'
		data = {
			'title': '머시기',
			'content': '머시기'
			'bar': 1
		}
		Foo.objects.create(**data)
		response = self.client.get(url)
		# status code check
		assert(response.status_code == 200)
		# returned response check
		assert(response.data['title'] == data['title'])
		assert(response.data['content'] == data['content'])
		assert(response.data['bar'] == data['bar'])

	def test_create_foo(self):
		client = self.client
		url = '/api/v1/foo/'
		data = {
			'title': '머시기',
			'content': '머시기',
			'bar': 1
		}
		response = self.client.post(url, data=data)
		assert(response.status_code == 201)
		foo = Foo.objects.last()
		assert(foo.title == data['title'])
		assert(foo.content == data['title'])
		assert(foo.bar.id == data['bar'])
  
  def test_create_foo_without_title(self):
    client = self.client
    url = '/api/v1/foo/'
    data = {
      'content': 'foobar'
      'bar': 2
    }
    response = self.client.post(url, data=data)
    assert(response.status_code == 400)

	def tearDown(self):
		"""
		이 method는 setUp과 반대로 class내 각 test function의 실행이 완료된 후에 실행됩니다.(on destroy)
    생성한 model instance를 삭제해주는 등의 작업이 들어갑니다.
		"""
		Foo.objects.all().delete()
```

## TDD
위의 테스트 코드는 기확자, client 개발자와 논의가 끝난 상황이면 코드 작성 이전에 먼저 작성할 수 있는 수준입니다.  
(url, data format만 약속되어 있으면 작성 가능)  
따라서 이 test code를 먼저 작성하고 test를 통과하도록 코딩을 한 뒤,  
refactoring을 한번 하는 방식을 TDD라고 합니다.(Test Driven Development)  
이 방식으로 개발을 할 경우 테스트 코드를 통한 코드의 견고함 뿐만이 아니라  
목표가 명확해지므로 중간에 길을 잃는 상황이 잘 생기지 않습니다.  

