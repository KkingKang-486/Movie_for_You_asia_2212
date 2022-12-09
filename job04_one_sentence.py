# 타이틀컬럼?이 2개~30개 격차가 큼, 30개를 한문장으로 리뷰를 다 합쳐
# 길어지더라도 하나의 문서로(document), 영화제목 문서, 영화 리뷰 문서 - 모델은 한 문장으로 볼 것
# 하나로 합쳐서 하나의 문장으로 보겠음
import pandas as pd

df = pd.read_csv('./crawling_data/cleaned_reviews_2016_2022.csv')
df.dropna(inplace=True)
df.info()

one_sentences = []                      # 하나의 문장으로 합쳐보겠
for title in df['titles'].unique():     # 유니크 함수 썼으니 한번만 나올 것
    temp = df[df['titles']==title]      # 템프로 받음
    if len(temp) > 30:    # 30개 제한 안하고 다긁었다면 이렇게 해도됨(제목)
        temp = temp.iloc[:30, :]
    one_sentence = ' '.join(temp['clean_reviews'])  # 컬럼명 조인함수로 이어붙임
    one_sentences.append(one_sentence)
df_one = pd.DataFrame({'titles':df['titles'].unique(), 'reviews':one_sentences})  # 리렇게 만들어진 리스트로 데이터 프레임 만들겠 # 타이틀스 컬럼의 유니크, 리뷰스 컬럼의 원센텐시스
print(df_one.head()) # 타이틀의 유니크한 값과
df_one.to_csv('./crawling_data/one_sentences.csv', index=False)

