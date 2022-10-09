# 국내 박스오피스 순위 확인 파일
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from datetime import date, timedelta
import warnings
warnings.filterwarnings(action='ignore')

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
        for i in range(len(final)):
            final[i] = f'{int(final[i]):,}명'
        return final

    if keyword == 'audiAcc': # 누적 관객수
        rule = re.compile('(?<=\<audiAcc>)(.*?)(?=<\/audiAcc>)')
        final = rule.findall(factor)
        for i in range(len(final)):
            final[i] = f'{int(final[i]):,}명'
        return final

# 테이블 확인용 (관객수 데이터 string)
table_data1 = {"순위" : crawling_boxoffice(date_keyword[0], 'rank'), "영화명" : crawling_boxoffice(date_keyword[0], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[0], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[0], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[0], 'audiAcc'), "기준 날짜" : date_list[0]}

table_data2 = {"순위" : crawling_boxoffice(date_keyword[1], 'rank'), "영화명" : crawling_boxoffice(date_keyword[1], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[1], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[1], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[1], 'audiAcc'), "기준 날짜" : date_list[1]}

table_data3 = {"순위" : crawling_boxoffice(date_keyword[2], 'rank'), "영화명" : crawling_boxoffice(date_keyword[2], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[2], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[2], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[2], 'audiAcc'), "기준 날짜" : date_list[2]}

table_data4 = {"순위" : crawling_boxoffice(date_keyword[3], 'rank'), "영화명" : crawling_boxoffice(date_keyword[3], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[3], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[3], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[3], 'audiAcc'), "기준 날짜" : date_list[3]}

table_data5 = {"순위" : crawling_boxoffice(date_keyword[4], 'rank'), "영화명" : crawling_boxoffice(date_keyword[4], 'movieNm'),
        "개봉일" : crawling_boxoffice(date_keyword[4], 'openDt'), "일일 관객수" : crawling_boxoffice(date_keyword[4], 'audiCnt'),
        "누적 관객수" : crawling_boxoffice(date_keyword[4], 'audiAcc'), "기준 날짜" : date_list[4]}

table1 = pd.DataFrame(table_data1) # 5일전 기준 박스오피스
table2 = pd.DataFrame(table_data2) # 4일전 기준 박스오피스
table3 = pd.DataFrame(table_data3) # 3일전 기준 박스오피스
table4 = pd.DataFrame(table_data4) # 2일전 기준 박스오피스
table5 = pd.DataFrame(table_data5) # 어제 박스오피스

table = pd.concat([table1, table2, table3, table4, table5])
table.to_csv('data_table.csv', index=False)

table_number1 = crawling_boxoffice(date_keyword[4], 'movieNm')[0] # 어제 기준 박스오피스 1위 작품
final_table1 = table[table['영화명'] == table_number1]

table_number2 = crawling_boxoffice(date_keyword[4], 'movieNm')[1] # 어제 기준 박스오피스 2위 작품
final_table2 = table[table['영화명'] == table_number2]

table_number3 = crawling_boxoffice(date_keyword[4], 'movieNm')[2] # 어제 기준 박스오피스 3위 작품
final_table3 = table[table['영화명'] == table_number3]

table_number4 = crawling_boxoffice(date_keyword[4], 'movieNm')[3] # 어제 기준 박스오피스 4위 작품
final_table4 = table[table['영화명'] == table_number4]

table_number5 = crawling_boxoffice(date_keyword[4], 'movieNm')[4] # 어제 기준 박스오피스 5위 작품
final_table5 = table[table['영화명'] == table_number5]

final_table1.to_csv('number1_table.csv', index=False)
final_table2.to_csv('number2_table.csv', index=False)
final_table3.to_csv('number3_table.csv', index=False)