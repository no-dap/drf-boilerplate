# Angular
Angular는 web SPA(Single Page Application)을 만들기 위한 framework입니다.  
기본적으로 javascript의 superset인 typescript를 기본 언어로 사용합니다.(javascript, dart 사용가능)  
1.x버전 단위인 AngularJS와는 전혀 다른 framework라고 보셔도 됩니다.(이후 버전들은 ngx라고 따로 부름.)  
Classic한 MVC pattern이 아닌 component로 화면을 구성하고, service로 data를 관리합니다.  
Learning curve가 시작부터 아주 가파른 framework이기 때문에 시간이 남는 경우 맛보기 정도로만 진행하겠습니다.  

## How to start
1. install node.js
2. install npm(node.js package manager) -> node.js 설치 시 자동으로 설치됩니다.
3. in command line : 
```
npm install -g @angular/cli
ng new my-project
cd my-project
ng serve
```
4. profit!
  
ng serve 명령어를 실행하면 local의 4200번 port로 node.js 서버가 열리며,  
해당 서버는 src directory 내의 코드를 compile하여 serve합니다.  
소스코드의 변경은 watcher가 자동으로 감지하여 recompile 후 서버를 다시 실행해줍니다. (thanks to @angular/cli)

## Dependency control
python이 package를 pip으로 관리하듯, javascript는 npm으로 관리합니다.  
필요한 library가 있을 경우 npm install {package name}@{version} --save 로 설치가 가능하며,  
--save 입력 시 requirement.txt같은 역할을 하는 package.json에 자동으로 버전 정보가 저장됩니다.  
(version을 입력하지 않을 시 @latest로 설치됩니다.)  

## Structure
Angular의 structure를 이루는 단위는 다음과 같습니다.
- Component : 실제 화면 구성 요소 코드를 포함합니다.
- Service : component간의 데이터 교환을 맡습니다.
- Directive : Angular 코드가 동작할 html 태그 지시자를 만듭니다? (한글로 설명하기가 힘드네요)
- Module : code tree 구성요소의 분기점? 을 맡습니다.
- guard, pipe, interface, etc...

## Scaffolding
```
ng generate component my-component
(or)
ng g c my-component
```
마찬가지로 각종 구성 요소를 위 명령어를 통해 생성할 수 있습니다.  
이 명령어로 생성되는 파일들은 service를 제외하면 생성한 위치와 가장 가까운 module에 자동으로 등록됩니다.  

## Observable
rxjs에서 제공하는 object type으로 subscription이 가능한 객체입니다.  
현대의 유행에 맞게 javascript code를 asynchronous, event-driven 하게 바꿔줍니다.  
기본적으로 Angular는 데이터 처리에 rx패턴을 사용하는 경우가 많아 처음에 익숙해지기가 어렵습니다.  

## StyleSheet
한 페이지에 지속적으로 render를 하는 Angular의 특성 상 기존의 class naming은 충돌의 우려가 있습니다.  
(일반적으로 사용하는 container 등)  
이것을 피하기 위해 sass나 less같은 BEM(Block Element Modifier)이 포함된 style의 사용을 권장합니다.  

## Component
Component는 template, style sheet, selector 등을 decorator를 통해 지정해 주어야 합니다.  
기본적으로 class를 사용하여 정의합니다. (ES6에서 2015년부터 추가됨)  
대부분의 application framework에서 지원하는 [Lifecycle Hooking](https://angular.io/guide/lifecycle-hooks)이 Angular에도 존재합니다.  
Template에서 일어나는 event를 제공받는 event binding과 데이터를 Template에서 제공하는 data binding이 존재합니다.  
각 binding의 event와 data는 모두 기본적으로 reactive하게 제공됩니다.  

## Service
Service는 데이터를 관리하는 역할을 합니다. 서버로 request를 보내 data를 가져와 component에 전달해주거나,  
component에서 모은 data를 가공하여 서버로 전송해주는 역할을 합니다.  
Injectable이라는 decorator를 붙여 component에 dependency injection이라는 형태로 제공됩니다.  
DI는 일종의 coding pattern으로 공통으로 사용할 수 있는 function을 매번 component에서 생성해 주는 것이 아니라  
service에 정의하여 component가 instantiate될 때 해당 function을 제공받는 형태입니다.  

## Routing
Angular application은 SPA이므로, local url 변경 시 실제로 서버에 request를 보낸 후 reload를 절대로 하면 안됩니다.  
따라서 이를 피하기 위한 strategy가 두 가지 존재합니다.  
1. base href  
Modern HTML5 browser들은 history.pushState()를 제공합니다. 이것은 browser history 상태 변경 api로,  
index.html에 base href를 삽입하면 Angular router가 이를 인지하여 url 변경 시 reload를 막습니다.
    ```
    <base href="/">
    ```
2. hash location
history.pushState()를 제공하지 않는 브라우저까지 지원하기 위해서는 hash location strategy를 이용해야 합니다.  
이것은 브라우저가 # 뒤에 붙은 url의 변경은 페이지 변경으로 간주하지 않아 reload를 하지 않는다는 점을 이용하는 방식입니다.  
router module을 불러올 때 useHash: true를 넣어주는 것으로 사용이 가능합니다.
    ```
    (in src/app/app.module.ts)
    
    @NgModule({
      imports: [
        ...
        RouterModule.forRoot(routes, { useHash: true })
        ...
      ],
      ...
    })
    ```
  
## Build
ng build 명령어를 통해 typescript 파일들을 javascript로 compile하고,  
compile된 javascript 파일들을 webpack으로 bundling하여  
별도의 node.js server의 serving 없이 바로 사용 가능한 형태로 빌드가 가능합니다.  


## Testing
:(  
물론 Angular도 Jasmine이라는 library를 통해 테스트를 지원합니다.  
TestBed라는 내부 testing class를 통해 component와 service등을 생성해서  
원하는대로 component가 그려지는 지, service가 제대로 동작하는 지 테스트합니다.  
또한 코드 테스트만이 아닌 유저 입장에서 사용하는 것처럼 흉내내는 e2e test도 존재합니다.  
하지만 front-end 특성 상 작은 코드수정에도 test가 와장창인 경우가 많습니다.  
(예를 들어 component 하나를 삭제하면 그 아래 존재하는 component의 위치 테스트는 모두 터지게 됩니다.)  
공수가 서버에 비해 너무너무너무 많이 들어가는 일이므로 어느정도 규모있는 프로젝트에서만 진행하는 것을 권장합니다.  
