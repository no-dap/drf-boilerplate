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


### transition
> element 형태를 변화시키는 property입니다.
> - rotate : 회전
> - skew : 찌그러뜨리기
> - scale : 확대
> - translate : 이동

### z-index
> element가 겹치는 경우 더 높은 z-index값을 가지는 element가 더 위로 옵니다.  
> positioned element에 대해서만 작동합니다.  
  
기타 CSS들은 좀더 detail한 부분들을 styling하므로 필요 시 검색해서 사용하시는 것이 좋습니다.  

