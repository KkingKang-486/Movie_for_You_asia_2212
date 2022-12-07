#자연어기반 영화추천시스템
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

#크롤링코드 만든다음에 크롤링 분담하여
options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)    # 드라이버 만들어놓

# 어디를 긁을 거냐면 : 네이버 영화 리뷰 -> 비슷한 리뷰를 가지고 있는 영화를 추천해줄 것 (ex)겨울왕국)
# 추천시스템 그전 알고리즘 방식 - 분유를 샀다면 기저귀를 살 가능성이 높. 포인트카드만들며 구매정보 활용할 수 있도록 사인하게됨 # 그 장바구니 정보로 : 통계적인 방법
# 인공지능. 자연어처리가 된다는 것. 말은 통계로 안됨(수식) 넷플릭스 추천컨텐츠 목록에 올라오는 것들
# 추천이라는 건 노출 많이 시켜주는 것. 원래 아마존에서 안사던 사람인데 띄워줘서 사는 30프로

url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2022&page=1'     # 페이지


깃만들기




