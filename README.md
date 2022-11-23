# Python과 Tableau를 이용하여 국내 박스오피스 순위 확인 구현  


- 영진위 오픈 API로 크롤링해서 테이블과 그래프를 확인하는 코드를 Pycharm을 이용하여 Python으로 코드 작성 및 tableau로 시각화 

- 테이블로 시각화 할때는 f-string을 통해 끝에 '명'이라는 단어와 천단위 ","설정 때문에 관객수 데이터 타입을 string으로 사용

- 그래프로 시각화 할때는 관객수 데이터 타입을 int로 사용

- 아쉬웠던 점 : 포스터 이미지도 OPEN API로 불러올 수 있었으면 참 좋았을텐데 그렇지 못해 데이터 업데이트처럼 수동으로 다운받아서 이미지를 교체해줘야 하는게 좀 아쉬웠고, Tableau Public 파일로 보면 정상적으로 한국 시간에 맞게 데이터가 설정되는데 Tableau Public 홈페이지에 게시하면 외국 사이트라 그런지 UTC가 적용되어 한국 시간 기준 오전 9시가 지나야 결과가 반영이 되는데 해결하지 못함..

![1](https://user-images.githubusercontent.com/109947297/203483045-20138bb7-2efe-4c3a-8fbc-3e90451fcaa9.png)
![2](https://user-images.githubusercontent.com/109947297/203483103-1139e2c3-689e-4a62-b612-21cc3ee323d4.png)
![3](https://user-images.githubusercontent.com/109947297/203483144-475f53d8-33f6-4cf7-9d19-f17afaf920d5.png)
![4](https://user-images.githubusercontent.com/109947297/203483166-fc378522-00c3-407d-9e1e-e84624efe84e.png)

## Tableau Public 링크
https://public.tableau.com/views/_16654068229660/1?:language=ko-KR&:display_count=n&:origin=viz_share_li

