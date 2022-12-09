import pandas as pd
import glob

data_paths = glob.glob('./crawling_data_2018,2019/*')

df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)    # nan값 제거
    df_temp.drop_duplicates(inplace=True)    # 중복제거
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()
print(len(df.titles.value_counts()))
df.to_csv('./crawling_data/review_2018,2019.csv', index=False)

# 403개, 리뷰 없는 200여개는 추천해주지 않아도될, 최근 6년 올해까지 7년
# 컨캣까지 해서 푸시날리고 팀장이 취합
# 년도별로 컨캣 or 따로줘도 팀장이 하나로 합칠 것
