# 국내 박스오피스 순위 확인 개인 프로젝트 

- 진행기간 : 2022.10.9 ~ 2022.10.10

- Python을 이용하여 영화진흥위원회 Open API 크롤링 및 데이터 전처리 진행 (IDE: Pycharm)
- 시각화 방식에 따라 테이블과 그래프 두 가지 경우로 나누어 데이터 전처리 진행

- <b>테이블</b> 시각화의 경우에는 f-string을 통해 끝에 '명'이라는 단어와 천단위 ","설정 때문에 관객수 데이터 타입을 <b>string</b>으로 사용하여 전처리 진행 

![코드1](https://user-images.githubusercontent.com/109947297/203526456-d4f1942b-dbac-4f99-bab4-227f19f85497.PNG)
![코드2](https://user-images.githubusercontent.com/109947297/203526501-36540dab-8e88-4654-a5a1-7a361af5cca9.PNG)

- <b>그래프</b> 시각화의 경우에는 데이터를 <b>int</b> 타입으로 전처리 진행

![코드3](https://user-images.githubusercontent.com/109947297/203527103-f5826998-ac27-4225-8e9c-0cde01a79f5a.PNG)
![코드4](https://user-images.githubusercontent.com/109947297/203527109-5fda2e7e-70d4-46ce-8a8d-04822b69d9e3.PNG)
![코드5](https://user-images.githubusercontent.com/109947297/203527115-f33194b7-cda7-4b1e-aaec-3e19f3a461da.PNG)
![코드6](https://user-images.githubusercontent.com/109947297/203527120-a1d0848a-f326-4487-8516-e4be10aee95d.PNG)


- 전처리된 데이터를 바탕으로 Tableau를 통해 시각화

![1](https://user-images.githubusercontent.com/109947297/203483045-20138bb7-2efe-4c3a-8fbc-3e90451fcaa9.png)
![2](https://user-images.githubusercontent.com/109947297/203483103-1139e2c3-689e-4a62-b612-21cc3ee323d4.png)
![3](https://user-images.githubusercontent.com/109947297/203483144-475f53d8-33f6-4cf7-9d19-f17afaf920d5.png)
![4](https://user-images.githubusercontent.com/109947297/203483166-fc378522-00c3-407d-9e1e-e84624efe84e.png)

부트캠프에서 <a href="https://github.com/anydevil0812/bootcamp_project/tree/main/Project3">국내 기후변화 예산&의안 분석 프로젝트</a>를 진행하면서 Open API를 이용한 크롤링을 다뤄볼 기회가 생겨 프로젝트가 종료된 후에 프로젝트를 진행하면서 습득한 것을 평소 저의 관심 분야인 영화와 접목해보고 싶었는데 마침 대체공휴일로 평소보다 시간도 생겼고 이전에 한번도 사용해보지 않았던 Tableau라는 플랫폼을 이용해보고 싶기도 하여 저만의 개인 프로젝트를 진행하게 되었습니다. 

처음에는 간단하게 금방 구현 할것이라 생각했지만 테이블과 그래프 시각화를 동일한 데이터 타입으로 진행하니 한쪽이 시각화가 정상적으로 실행되면 다른 한쪽이 시각화 실행이 안되는 문제에 직면하였다가 결국 테이블 시각화에 필요한 데이터와 그래프 시각화에 필요한 데이터의 타입을 서로 다르게 하여 진행하여 해결하였습니다. 

개인적으로 포스터 이미지도 OPEN API로 불러올 수 있었으면 참 좋았을텐데 영화진흥위원회 OPEN API에서 제공을 하지 않아 포스터 이미지를 수동으로 다운받아서 이미지를 교체해줘야 하는게 좀 아쉬웠고

Tableau Public이나 Tableau Reader 파일로 보면 정상적으로 한국 시간에 맞게 결과물을 정상적으로 확인이 가능한데 Tableau Public 홈페이지에 게시하면 외국 사이트라 그런지 UTC가 적용되어 한국 시간 기준 오전 9시가 지나야 결과가 반영되었고 이를 해결하지 못한게 아쉬웠지만 코딩을 배우면서 만들어보고 싶었던 결과물 구현에 성공하고 Tableau라는 플랫폼도 한번 경험해본 만족스러운 경험이었습니다.  

## Tableau Public 링크
https://public.tableau.com/views/_16654068229660/1?:language=ko-KR&:display_count=n&:origin=viz_share_li
