# Tableau 국내 박스오피스 그래프 생성용 데이터 csv파일 생성 (관객수 데이터 int)
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from datetime import date, timedelta

# 5일간의 날짜 목록
date_list = []
for i in range(1,6):
    date_list.append(date.today()-timedelta(i))
date_list.sort()

# OPEN API 파라미터 입력을 위한 datetime -> str
date_list = list(map(str, date_list))
date_keyword = []
for i in range(len(date_list)):
    date_keyword.append(date_list[i].replace('-', ''))

keywords = ['rank', 'movieNm', 'openDt', 'audiCnt', 'audiAcc']

# 영화진흥위원회_영화박스오피스 DB OPEN API 이용하여 크롤링
def crawling_boxoffice(date, keyword):

    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml'
    params ={'key' : 'ee0e8dd4b1074b2a1378799562c3d370', "targetDt" : date}
    response = requests.get(url, params=params) # UTF-8 코드 형식로 데이터가 불러와짐
    soup = BeautifulSoup(response.content, 'xml')

    factor = soup.select(keyword)
    factor = str(factor)

    if keyword == 'rank': # 순위
        rule = re.compile('(?<=\<rank>)(.*?)(?=<\/rank>)')
        final = rule.findall(factor)
        for i in range(len(final)):
            final[i] += "위"
        return final

    if keyword == 'movieNm': # 영화명
        rule = re.compile('(?<=\<movieNm>)(.*?)(?=<\/movieNm>)')
        final = rule.findall(factor)
        return final

    if keyword == 'openDt': # 개봉일
        rule = re.compile('(?<=\<openDt>)(.*?)(?=<\/openDt>)')
        final = rule.findall(factor)
        return final

    if keyword == 'audiCnt': # 일일 관객수
        rule = re.compile('(?<=\<audiCnt>)(.*?)(?=<\/audiCnt>)')
        final = rule.findall(factor)
        final = list(map(int, final))
        return final

    if keyword == 'audiAcc': # 누적 관객수
        rule = re.compile('(?<=\<audiAcc>)(.*?)(?=<\/audiAcc>)')
        final = rule.findall(factor)
        final = list(map(int, final))
        return final

data1 = {"순위" : crawling_boxoffice(date_keyword[0], 'rank'), "영화명" : crawling_boxoffice(date_keyword[0], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[0], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[0], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[0], 'audiAcc'), "기준 날짜" : date_list[0]}

data2 = {"순위" : crawling_boxoffice(date_keyword[1], 'rank'), "영화명" : crawling_boxoffice(date_keyword[1], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[1], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[1], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[1], 'audiAcc'), "기준 날짜" : date_list[1]}

data3 = {"순위" : crawling_boxoffice(date_keyword[2], 'rank'), "영화명" : crawling_boxoffice(date_keyword[2], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[2], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[2], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[2], 'audiAcc'), "기준 날짜" : date_list[2]}

data4 = {"순위" : crawling_boxoffice(date_keyword[3], 'rank'), "영화명" : crawling_boxoffice(date_keyword[3], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[3], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[3], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[3], 'audiAcc'), "기준 날짜" : date_list[3]}

data5 = {"순위" : crawling_boxoffice(date_keyword[4], 'rank'), "영화명" : crawling_boxoffice(date_keyword[4], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[4], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[4], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[4], 'audiAcc'), "기준 날짜" : date_list[4]}

table1 = pd.DataFrame(data1)
table2 = pd.DataFrame(data2)
table3 = pd.DataFrame(data3)
table4 = pd.DataFrame(data4)
table5 = pd.DataFrame(data5)
table = pd.concat([table1, table2, table3, table4, table5])

number1 = crawling_boxoffice(date_keyword[4], 'movieNm')[0] # 어제 기준 박스오피스 1위 작품
final_table1 = table[table['영화명'] == number1]
final_table1.to_csv('number1.csv', index=False) # 어제 기준 박스오피스 1위 작품 5일간 관객수 추이 csv 파일

number2 = crawling_boxoffice(date_keyword[4], 'movieNm')[1] # 어제 기준 박스오피스 2위 작품
final_table2 = table[table['영화명'] == number2]
final_table2.to_csv('number2.csv', index=False) # 어제 기준 박스오피스 2위 작품 5일간 관객수 추이 csv 파일

number3 = crawling_boxoffice(date_keyword[4], 'movieNm')[2] # 어제 기준 박스오피스 3위 작품
final_table3 = table[table['영화명'] == number3]
final_table3.to_csv('number3.csv', index=False) # 어제 기준 박스오피스 3위 작품 5일간 관객수 추이 csv 파일