import pandas as pd
from gensim.models import Word2Vec

review_word = pd.read_csv('./crawling_data/one_sentences.csv')      # 난 아직 오류나서 안만들어짐
review_word.info()

#4103개로 줄어듦 # 타이틀은 필요없고 리뷰만 좀 뽑아내겠
# one_sentence_reviews = review_word['reviews']
one_sentence_reviews = list(review_word['reviews']) # 리스트로 바꾸면
cleaned_tokens = []
for sentence in one_sentence_reviews:     # 문자열이 들어가 있는 걸 형태소 단위로 자를 것(현재 띄어쓰기 되어있)
    token = sentence.split()              # 띄어쓰기 기준으로 다 자름
    cleaned_tokens.append(token)

# 임베딩 모델 만들 것. 유사한 단어들을 근처에 배치하는 워드투벡
embedding_model = Word2Vec(cleaned_tokens, vector_size=100,    # 형태소 개수만큼 차원이 만들어짐. # 벡터 사이즈 100 = 차원축소하겠다는 말
                            window=4, min_count=20,
                            workers=4, epochs=100, sg=1)  # 단어를 벡터화 해주는 임베딩모델 Word2vec # 각 영화의 리뷰를 한 문장씩 = 형태소들의 리스트로 만들어서 줄 것
    # 윈도우. 10개의 단어를 잘라서 보고 (콘브1d의 커널 방식과 비슷한)
    # 말뭉치 20개 이하는 버리겠다는 20개 위부터 학습을 하겠다
    # min_count = 말뭉치 20개 이하는 버리겠다
    # 워커스 = cpu 몇개 쓸거냐
    # sg = 벡터화하는 알고리즘 지칭


# 유사한 단어 많이 있는 리뷰 추천 해준다
embedding_model.save('./models/word2vec_movie_review.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))     # 몇개 있는 지 보려면

# 거리&시각화








