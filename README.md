<h1>  National-Petition </h1>

[국민청원 분석 보고서](https://github.com/newhiwoong/National-Petition/blob/master/REPORT_V1.md)


[국민청원 사이트](https://www1.president.go.kr/petitions) 분석에 설정과 코드에 대한 간단한 설명을 진행합니다.

## Petition Data
국민청원을 분석하기 위해 국민청원 사이트를 [크롤링한 데이터](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)를 다운로드합니다.

## Install files
 기본적으로 Git이 설치되있다고 가정하겠습니다. 국민청원 분석을 하는 코드를 저장할 하위 폴터에서 아래 코드를 실행시킵니다.

```
git init
git clone https://github.com/newhiwoong/National-Petition.git
```

 그럼 `National-Petition` 폴터가 생성될 것입니다. 이제 [국민청원 Data](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)를 `National-Petition` 폴더 내부에 넣습니다.
 
## Folder structure
``` bash
  |-Data-Analysis                          #데이터 분석 및 그래프를 제작
  |  |-images                              #분석 결과 이미지
  |  |  |-graph_*.png                      #여러 그래프 이미지
  |  |  |-num_*.JPG                        #추천수별 이미지
  |  |-Create_a_graph.ipynb                #분야별 추천수 그래프를 만드는 코드
  |  |-Create_a_graph_month.ipynb          #월별 추천수 그래프를 만드는 코드
  |  |-Data_Analysis.ipynb                 #그래프에 필요한 분야별 CSV 파일 제작
  |  |-Data_Analysis_month.ipynb           #그래프에 필요한 월별 CSV 파일 제작
  |  |-README.md                           #데이터 분석 및 그래프 제작을 설명하는 문서
  |  |-participants.csv                    #Data_Analysis에서 만든 CSV 파일
  |  |-participants_index.csv              #Data_Analysis에서 만든 index가 추가 된 CSV 파일
  |  |-participants_month.csv              #Data_Analysis_month에서 만든 CSV 파일
  |  |-participants_month_index.csv        #Data_Analysis_month에서 만든 index가 추가 된 CSV 파일
  |-Data                                   #국민 청원 데이터 크롤링
  |  |-Crawling.ipynb                      #크롤링을 하는 코드
  |  |-Filtering.ipynb                     #추천수를 str형에서 int형으로 변환하는 코드
  |  |-README.md                           #국민 청원 데이터 크롤링을 설명하는 문서
  |  |-briefing2.csv                       #브리핑한 청원을 크롤링한 CSV 파일
  |-Find-similar                           #비슷한 청원 찾기
  |  |-README.md                           #비슷한 청원 찾기를 설명하는 문서
  |-Government-Thinking                    #정부의 생각 알아보기
  |  |-img                                 #브리핑한 청원에 대한 워드클라우드 이미지들
  |  |-Data_Analysis.ipynb                 #분야별 추천수 그래프를 만드는 코드
  |  |-README.md                           #정부의 생각 알아보기를 설명하는 문서
  |  |-Word_Cloud.ipynb                    #브리핑한 청원에 대한 워드클라우드를 만드는 코드
  |  |-briefing.csv                        #브리핑한 청원을 크롤링한 CSV 파일
  |  |-crawling.ipynb                      #브리핑한 청원을 크롤링하는 코드
  |....
  |-REPORT_V1.md                           #국민청원을 분석한 내용
```

## Required package
기본적으로 ANACONDA 환경에 jupyter notebook에서 진행합니다. 이를 위해 [ANACONDA 설치](https://www.anaconda.com/download/) 및 환경 설정이 필수적으로 필요합니다.

그리고 주로 [KoNLPy](http://konlpy.org/en/latest/)를 많이 사용하는데 이를 위해 [Java](https://www.java.com/ko/download/) 설치 및 환경설정이 필요합니다. 

이후 필요한 내용은 [Installation Code](https://github.com/newhiwoong/National-Petition/blob/master/installation_code.ipynb)를 실행하시면 필요한 Package들이 설치됩니다.

### Install Terminal 
```
sudo apt-get update
sudo apt-get install oracle-java8-installer

pip install nltk
pip install konlpy
pip install wordcloud
pip install urllib
pip install bs4
pip install multiprocessing
```

## CODE
청원 분석에 대해 제작할 코드들입니다.

### Todo list

- [x] 국민청원 게시판 크롤링 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Data)
- [x] 국민청원 데이터 분석 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Data-Analysis)
- [x] 국민청원 워드클라우드 제작 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Word-Cloud)
- [x] 국민청원 네트워크 제작 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Network)
- [x] 국민의 생각 알아보기 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/National--Thinking)
- [x] 정부의 생각 알아보기 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Government-Thinking)
- [x] 국민청원 중요 키워드 분석 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Important-Keywords)
- [x] 국민청원 게시판 분석 내용 [DOCS](https://github.com/newhiwoong/National-Petition)
- [ ] 영어 키워드 찾기 
- [ ] 청원 분류
- [ ] 비슷한 청원 찾기
- [ ] 강화된 네트워크 제작
- [ ] 국민청원과 지지율의 상관관계 찾기
- [ ] 국민의 뜻과 정부의 생각과 괴리 찾기
- [ ] 통합 웹 사이트 제작
- [ ] 해석하는 인공지능 제작
- [ ] 루머 청원 찾기 