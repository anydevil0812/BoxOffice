# 국내 박스오피스 순위 확인 개인 미니 프로젝트
![99](https://user-images.githubusercontent.com/109947297/210086961-747c3715-ff7d-4d54-966d-c1a160e6081b.jpg)
![333](https://user-images.githubusercontent.com/109947297/210086967-05488033-2fa1-44be-b114-cad934ab09fb.jpg)

## [Tableau Public 링크]

https://public.tableau.com/views/_16654068229660/1?:language=ko-KR&:display_count=n&:origin=viz_share_li

### [진행 기간]

- 2022.10.9 ~ 2022.10.10

### [프로젝트 소개]

부트캠프에서 **국내 기후변화 예산&의안 분석 프로젝트**를 진행하면서 **Open API를 이용한 크롤링**을 다뤄볼 기회가 생겨 프로젝트가 종료된 후에 프로젝트를 진행하면서 습득한 것을 평소 **저의 관심 분야인 영화와 접목**해보고 싶었는데 
<br><br> 마침 **대체공휴일로 평소보다 시간도 생겼고 이전에 한번도 사용해보지 않았던 **Tableau**라는 플랫폼을 이용해보고 싶기도 하여 저만의 개인 프로젝트를 진행하게 되었습니다.
<br><br> **Python**을 이용하여 영화진흥위원회 **Open API** 크롤링한 뒤 데이터 전처리를 진행<b>(IDE: Pycharm)</b>한 후 **Tableau로 시각화**하는 것이 목표였고 결과적으로 코딩을 배우면서 **평소에 만들어보고 싶었던 결과물** 구현에 성공하고 **Tableau**라는 플랫폼도 한번 경험해본 만족스러운 경험이었습니다.

### [사용한 Python Package]

- **BeautifulSoup, requests**를 이용한 크롤링
- **re 정규표현식**을 이용한 데이터 전처리
- **pandas**를 이용한 데이터프레임 생성
- **date, timedelta**를 이용한 날짜 데이터 처리

### [프로젝트 진행 중 겪은 문제점 및 아쉬웠던 점]
### 개발 문제
1. **테이블과 그래프** 시각화를 **동일한 데이터 타입으로 진행**하니 한쪽이 시각화가 정상적으로 실행되면 **다른 한쪽이 시각화 실행이 안되는 문제**에 직면했었습니다.
<br><br> => 결국 테이블 시각화에 필요한 **데이터와 그래프 시각화에 필요한 데이터의 타입을 서로 다르게** 하여 코드를 구성함으로써 해결하였습니다.

2. 테이블과 시각화 모두 같은 타입의 데이터로 개발을 진행하려 했으나 int로 진행하면 테이블에 명이라는 글자를 추가하는데 문제가 생겼고 string으로 진행하면 그래프 생성이 되지 않는 문제를 겪었습니다.
<br><br> => **테이블** 시각화의 경우에는 f-string을 통해 끝에 '**명**'이라는 단어와 천 단위 "**,**"설정 때문에 관객수 데이터 타입을 **string**으로 사용하여 전처리 진행하였고 **그래프** 시각화의 경우에는 데이터를 **int** 타입으로 전처리 진행함으로써 문제를 해결하였습니다.

### 아쉬웠던 점
1. 개인적으로 **포스터 이미지**도 OPEN API로 불러올 수 있었으면 참 좋았을 텐데 영화진흥위원회 **OPEN API에서 제공을 하지 않아** 
<br><br> => 포스터 이미지를 **수동으로 다운로드** 받아서 **이미지를 교체**해줘야 하는 게 좀 아쉬웠습니다.

2. **Tableau Public이나 Tableau Reader** 파일로 보면 정상적으로 **한국 시간**에 맞게 결과물을 정상적으로 확인이 가능한데 
<br><br> => **Tableau Public 홈페이지**에 게시하면 외국 사이트라 그런지 **UTC**가 적용되어 한국 시간 기준 **오전 9시가 지나야 결과가 반영**되었고 이를 해결하지 못해 아쉬웠습니다.

