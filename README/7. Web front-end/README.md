# Web front-end
web browser들은 아시다시피 html + css + javascript를 기본으로 화면을 구성합니다.  
기초적인 내용에 대한 설명보다는 자주 사용하는 css property, jquery의 사용법에 대해 정리했습니다.  

## CSS
CSS는 HTML을 styling해주는 언어로 자주 사용되는 property는 아래와 같습니다.

### display
> display는 해당 element가 보여지는 방식을 나타내는 property입니다.  
> - none : 숨기기
> - block : 새로운 line에서 element가 시작하며 부모의 width를 모두 차지합니다.
> - inline : 한줄로 표시되며 height나 width 관련된 property가 전부 disable됩니다.
> - flex : [link](https://d2.naver.com/helloworld/8540176) 참조
> - table : children을 &lt;table&gt;처럼 배치합니다.
> - inline-block : inline처럼 배치되나 width와 height를 지정할 수 있습니다.
> - inline-flex : inline처럼 배치되는 flex형태입니다.

### margin, border, padding
> 셋 모두 contents 바깥을 둘러싸는 구조를 지정할때 쓰이는 property입니다.  
> 해당 element의 테두리 선인 border를 기준으로 그 내부의 공간은 padding으로, 그 외부의 공간은 margin으로 지정합니다.  
> (개발자 도구 참고)

### position
> position은 해당 element가 위치하는 방식을 지정하는 property입니다.
> - static : 디폴트 값으로 document가 그려지는대로 위치합니다.
> - absolute : 가장 가까운 position이 static이 아닌 조상을 기준으로 absolute한 위치를 갖습니다.
> - relative : static한 position에서 상대적인 위치를 갖습니다.
> - fixed : 부모 element를 무시하고 유저 window 기준으로 absolute한 위치를 갖습니다.
> 
> static을 제외한 나머지는 top, left, bottom, right의 속성에 영향을 받습니다. (실제로 위치를 지정해줄 수 있음)  


### overflow
> element를 넘치는 contents의 처리에 대한 property입니다.
> - visible : 무시하고 다 보여줍니다.
> - hidden : 넘치는 만큼 잘라서 숨깁니다.
> - scroll : 넘치는 만큼 숨기고, scroll을 추가합니다.


### transform
> element 형태를 변화시키는 property입니다.
> - rotate : 회전
> - skew : 찌그러뜨리기
> - scale : 확대
> - translate : 이동

### z-index
> element가 겹치는 경우 더 높은 z-index값을 가지는 element가 더 위로 옵니다.  
> positioned element에 대해서만 작동합니다.  
  
기타 CSS들은 좀더 detail한 부분들을 styling하므로 필요 시 검색해서 사용하시는 것이 좋습니다.  

## Javascript
Javascript는 웹 브라우저의 동적 scripting을 위해 주로 사용되는 언어입니다.  
익숙하지 않으셔도 Python같은 OOP, Dynamic typed language이기 때문에 금방 적응하실 수 있으리라 믿습니다.  
  
Python이 class를 기반으로 Object oriented 되어있다면,  
Javascript는 function을 기반으로 Object oriented 되어있는 언어인데, 이를 잘 알 수 있는 부분이 prototype입니다. 
  
또한 기본적으로 함수들이 asynchronous하게 돌기 때문에 callback 처리가 아주 중첩(callback hell)되는데,  
이를 해결하기 위한 [Promise pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)과 [async-await pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)은 각각 ES6, ES8에서 추가되었기 때문에  
old browser(공공의 적 ie)에서 지원이 되지 않기 때문에 callback에 익명 함수의 사용을 자제해야 합니다.  

### Cross Browser Compatibility
웹 브라우저의 종류와 각 브라우저 버전의 갯수만큼의 다양한 종류의 interpreter에서 실행되어야 하는 javascript의 특징때문에  
cross browser 지원은 꽤 중요하고 스트레스 받는 issue입니다.  
예를 들어 10버전 이하의 ie에서 HTMLDomElement.appendChild() is not a function 같은 문제는 유명합니다.  
해결 방법은  
1. 브라우저 강제하기
2. 해당 함수들 제거
3. polyfill 추가  
  
세 가지가 있습니다. 
이중 polyfill은 내장 interpreter에 저장되지 않은 함수를 직접 정의한 코드를 추가하는 방법으로,  
해당 error내용 + polyfill로 구글링하면 남들이 미리 작성한 코드를 사용할 수 있습니다.  

### JQuery
jquery는 가장 널리 사용되는 javascript framework중 하나입니다.  
단순하게 하나의 페이지에서의 동적 interaction을 당담하므로 사용법이 아주 간단하다는 장점이 있습니다.  
다만 조금 복잡한 기능을 하는 web application을 만들기에는 무리가 있으며,  
웹 특유의 화면 전환시 깜빡거림을 해결할 수 없고, 복잡한 animation 처리가 힘듭니다.  
  
화면의 특정 element를 jquery Object로 가져오고, 해당 Object의 prototyped function들을 통해 조절합니다.  
```
$('document').ready(function () {
    // browser cookie에서 csrf token을 가져옵니다.
    let csrftoken = $.cookie('csrftoken');

    $.ajaxSetup({
        /* *
        * ajax 요청을 실행하기 전에 header에 항상 X-CSRFToken을 심어줍니다.
        * 같은 방식으로 
        beforeSend: function (request, settings) {
            request.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    
    /* *
    * jquery나 pure javascript 모두 selector를 query해서 element를 가져옵니다.
    * id를 query할 경우 앞에 #을, class를 query할 경우 앞에 .을 붙여서 찾습니다.
    * 혼용도 가능합니다.
    */
    const submitButton = $('#submitButton'); // return : id가 submitButton인 jquery element Object
    const someClasses = $('.someClass'); // return : class가 someClass인 jquery element Object Array
    const someSpecificClasses = $('.someClass.specific'); // return : class에 someClass, specific 둘 다 있는 것
    const checkboxes = $('input[type="checkbox"]'); // return : checkbox들
    const someClassImages = $('.someClass > img'); // return: someClass인 element를 부모로 갖는 img tag를 가진 element들
    
    /* *
    * object든 object Array든 특정 method에 대한 동작은 똑같이 붙일 수 있습니다. (Array의 경우 모두 적용됨)
    */
    submitButton.on('click', callBackFunction());
    someClasses.on('scroll', callBackFunction());
    
    // on 말고 해당 행동들도 모두 method로 구현되어 있습니다.
    submitButton.click(callBackFunction());
    
    // 발생한 event를 argument로 받아 사용할 수도 있습니다.
    submitButton.on('keypress', function (event) {
        let e = event || window.event;
        // enter의 경우 event.which가 13입니다.
        if (e.which === 13) {
            doSomething();
        }
    });
    
    // 단순하게 스타일을 변경하는 것도 가능합니다.
    someClasses.on('scroll', function () {
        this.addClass('somethingFancy');
        // 또는 jquery object의 첫 번째 값은 항상 실제 element reference이므로, 다음같이 변경도 가능합니다.
        this[0].classList.add('somethingFancy');
        this[0].style.marginTop = '20px';
    });
    
    // 또는 ajax 요청을...
    submitButton.on('click', function () {
        $.ajax({
            url: '/api/v1/~',
            type: 'POST',
            data: {
                'foo': 'bar',
                'baz': 1
            },
            success: successCallBack(),
            error: errorCallBack()
        });
    });
});
```

## Webpack, minification, 난독화
웹페이지를 구성하는 css, js파일이 많아지면 자연스럽게 로딩이 길어지게 되는데,  
이 때문에 처음부터 각 하나의 파일에 코딩을 하게되면 유지보수가 너무나도 어려워집니다.  
이것을 해결하기 위해 분리된 각 assets를 하나의 bundle로 만들어 주는 library가 webpack인데,  
1. django가 각 static file을 serving함  
2. 프로젝트의 규모가 그리 크지 않음  
  
의 이유로 webpack은 사용하지 않습니다. (추후 react나 angular를 배우신다면 그 때 사용하세요)
마찬가지로 작은 규모의 웹페이지이므로 minification도 따로 하지 않고,  
항상 안전한 코드를 작성해서 난독화도 굳이 하지 않도록 노력해야 합니다.  

## TODO
1. 기존 서버에서 간단하게 정보를 표시하고 post, patch, delete 할 수 있는 화면 구성해보기 (+ mobile)
2. 작성한 웹 페이지를 포함한 코드를 deploy해서 결과 보기
