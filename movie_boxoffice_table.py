# Tableau 어제 기준 국내 박스오피스 테이블 생성용 데이터 csv파일 생성 (관객수 데이터 str)
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date, timedelta

# OPEN API 파라미터 입력을 위한 datetime -> str
yesterday = date.today()-timedelta(1)
yesterday_keyword = str(yesterday).replace('-', '')

# 영화진흥위원회_영화박스오피스 DB OPEN API 이용하여 크롤링
def crawling_boxoffice(keyword):

    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml'
    params ={'key' : 'ee0e8dd4b1074b2a1378799562c3d370', "targetDt" : yesterday_keyword}
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

# 테이블 생성용 csv 파일 생성 (관객수 데이터 str)
table_data = {"순위" : crawling_boxoffice('rank'), "영화명" : crawling_boxoffice('movieNm'),
        "개봉일" : crawling_boxoffice('openDt'), "일일 관객수" : crawling_boxoffice('audiCnt'),
        "누적 관객수" : crawling_boxoffice('audiAcc'), "기준 날짜" : yesterday}
table = pd.DataFrame(table_data)
table.to_csv('table_data.csv', index=False) # 어제 기준 박스오피스 순위 csv 파일