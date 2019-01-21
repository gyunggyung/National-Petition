# National-Petition

[![Stargazers](https://img.shields.io/badge/National--Petition-Stargazers-yellow.svg)](https://github.com/newhiwoong/National-Petition/stargazers)
[![license](https://img.shields.io/badge/license-Apache%202.0-red.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![results](https://img.shields.io/badge/results-Report-blue.svg)](https://paper.dropbox.com/doc/National-Petition-Analysis--AWBChEBfGCjv1j~TH2oJMUKbAg-RYdzoQNc8lAHVcDucJu1K)
[![data](https://img.shields.io/badge/data-web-brightgreen.svg)](https://www1.president.go.kr/petitions)

> 국민청원 및 제안 목록을 분석하여 국민의 생각을 알아보는 프로젝트

*링크를 클릭하시면 더 자세한 분석 결과를 확인할 수 있습니다 : [보고서](https://paper.dropbox.com/doc/National-Petition-Analysis--AWBChEBfGCjv1j~TH2oJMUKbAg-RYdzoQNc8lAHVcDucJu1K)*

## 📖 Introduction

 문재인 정부에서는 국민과의 소통을 통하여 국정에 반영하고자 청와대 홈페이지에 국민소통광장을 마련하였습니다. 국민소통광장의 ‘국민청원 및 제안’에서는 국민 누구나 청원을 올릴 수 있으며, 청와대로부터 답변을 받을 수 있습니다. 2019년 1월 1일 현재, 371,229개의 청원이 있으며, 본 연구에서는 웹 크롤링(web crawling)을 통해 국민이 올린 모든 글을 모두 데이터화하여 분석하여, 국민의 청원을 과학적으로 분석합니다. 특히, 국민 청원 글을 단어 단위로 분석하여, 국민의 관심이 집중되는 키워드와 키워드 간의 관계 네트워크, 더 나아가 분류된 분야별 단위의 키워드를 분석하여, 국민 청원의 단순한 통계가 아닌, 국민의 글 전체를 포괄하는 단어 수준의 분석을 수행합니다. 

 국민청원 게시판의 모든 글은 청와대의 관리를 받아 청원과 관련되지 않은 글은 삭제되거나, 주제에 맞지 않은 글을 주제에 맞게 재분류됩니다. 이러한 면에서 국민청원 데이터는 국민의 의견을 분석하기에 용이한 장점을 가지고 있습니다. 국민의 생각이 국정에 더 깊이 반영하는 것입니다. 국민청원의 모든 내용을 정부에서 검토하지 않을 것입니다. 하지만 국민들의 뜻을 요약하고 한 눈에 볼 수 있다면 충분히 정부 측에서도 일반 국민들의 뜻을 알 수 있을 것입니다. 또한 4차산업혁명, 인공지능 등이 실질적으로 우리의 삶에 어떠한 영향을 끼칠 수 있는지를 보여주며 대한민국의 미래 발전에 크게 이바지할 기회라고 생각합니다.

 인공지능 자연어처리를 통하여 글의 내용을 파악하는 연구는 다양한 분야에서 수행되어 왔으며, 기계학습 및 인공지능의 발전과 함께 많은 응용 분야에 적용되고 있습니다. 그러나 아직까지 자연어처리를 통한 연구는 데이터의 수집이 용이한 특정분야에 한정 돼있으며, 특히 정치 분야에는 아직 활발히 진행되지 못하고 있다. 그러나, 이번 국민소통광장을 통하여 본 연구소는 양질의 데이터를 확보하여, 정치분야의 연구를 통해 국민의 소리에 더 기울일 수 있는 기회를 제공하는 것이 이번 연구의 목적 중 하나라고 할 수 있습니다. 국민 청원 데이터는 첫째 청와대의 관리를 받고 있기에(데이터 전처리) 양질의 데이터 확보의 커다란 장점을 갖고 있습니다. 또한 국민의 추천수를 통해 글의 파급력이나 국민의 의견(동의)을 과학적으로 분석할 수 있는 기회를 제공합니다. 마지막으로 주제별/ 분야별로 청원이 분류되어 있어 분야별 분석을 용이하게 할 뿐 아니라 추후 지도학습 (supervised learning)도 고려할 수 있습니다. 


## 💾 Petitions data analysis

 먼저 국민청원을 분석하기 위해 국민청원 사이트를 [크롤링한 데이터](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)를 다운로드합니다.

 기본적으로 Git이 설치되있다고 가정하겠습니다. 국민청원 분석을 하는 코드를 저장할 하위 폴터에서 아래 코드를 실행시킵니다.

```
git init
git clone https://github.com/newhiwoong/National-Petition.git
```

 그럼 `National-Petition` 폴터가 생성될 것입니다. 이제 [국민청원 Data](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)를 `National-Petition` 폴더 내부에 넣습니다.
 
## 📂 Directory structure
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
  |-National-Petition-Important-Keywords   #중요 키워드를 분석하여 국민의 뜻 알아보기
  |  |-README.md                           #중요 키워드를 분석하기를 설명하는 문서
  |-National--Thinking                     #청원의 추천수별 키워드를 보며 국민의 관심사 분석
  |  |-README.md                           #청원의 추천수별 키워드를 보며 국민의 관심사 분석에 대해서 분석을 설명하는 문서
  |  |-Word_Cloud.ipynb                    #추천수별 워드클라우드를 만드는 코드
  |  |-briefing.csv                        #브리핑한 청원을 크롤링한 CSV 파일
  |  |-graph.ipynb                         #어떤 경우에 추천이 많은지를 분석하는 그래프를 제작하는 코드
  |-National-Petition-Network              #국민 청원에서 등장하는 키워드의 네트워크를 제작
  |  |-README.md                           #키워드 네트워크를 설명하는 문서
  |-Word-Cloud                             #분야별, 월별 키워드의 워드클라우드 제작
  |  |-Birthstone                          #월별 워드클라우드 이미지
  |  |  |-*.png                            #해당하는 월에 대한 워드클라우드
  |  |-img                                 #분야별 워드클라우드 이미지
  |  |  |-*.png                            #해당하는 분야에 대한 워드클라우드
  |  |-README.md                           #워드클라우드에 대해 설명하는 문서
  |  |-Word_Cloud.ipynb                    #분야별 워드클라우드를 제작하는 코드
  |  |-Word_Cloud_month.ipynb              #월별 워드클라우드를 제작하는 코드
  |-LICENSE                                #Apache License 2.0
  |-README.md                              #이 문서
  |-REPORT_V1.md                           #국민청원을 분석한 내용
  |-installation_code.ipynb                #필요한 페키지를 설치하는 코드
```

## 👨‍💻 System requirements
기본적으로 ANACONDA 환경에 jupyter notebook에서 진행합니다. 이를 위해 [ANACONDA 설치](https://www.anaconda.com/download/) 및 환경 설정이 필수적으로 필요합니다.

그리고 주로 [KoNLPy](http://konlpy.org/en/latest/)를 많이 사용하는데 이를 위해 [Java 설치](https://www.java.com/ko/download/) 및 환경설정이 필요합니다. 윈도우 사용자의 경우  [KoNLPy 설치](https://konlpy-ko.readthedocs.io/ko/v0.4.3/install/) 문서를 따라 설치를 하신 후 아래 내용을 진행하시길 바랍니다.

이후 필요한 내용은 [Installation Code](https://github.com/newhiwoong/National-Petition/blob/master/installation_code.ipynb)를 실행하시면 필요한 Package들이 설치됩니다.

### 👩‍💻 Dependency Build Instructions

#### Ubuntu
```
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install fonts-nanum-coding
```

#### All
```
pip install nltk
pip install konlpy
pip install wordcloud
pip install urllib
pip install bs4
pip install multiprocessing
```


## 📝 Todo list
청원 분석에 대해 제작할 코드와 문서들입니다.

- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/Data) 국민청원 게시판 크롤링 
- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/Data-Analysis) 국민청원 데이터 분석 
- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/Word-Cloud) 국민청원 워드클라우드 제작 
- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/Network) 국민청원 네트워크 제작 
- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/National--Thinking) 국민의 생각 알아보기 
- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/Government-Thinking) 정부의 생각 알아보기 
- [x] [💻](https://github.com/newhiwoong/National-Petition/tree/master/Important-Keywords) 국민청원 중요 키워드 분석 
- [x] [📗](https://github.com/newhiwoong/National-Petition) 국민청원 게시판 분석 내용 
- [ ] [🔨]() 영어 키워드 찾기 
- [ ] [🔨]() 청원 분류 
- [ ] [🔨]() 비슷한 청원 찾기 
- [ ] [🔨]() 강화된 네트워크 제작
- [ ] [🔒]() 국민청원과 지지율의 상관관계 찾기 
- [ ] [🔒]() 국민의 뜻과 정부의 생각과 괴리 찾기 
- [ ] [🔒]() 통합 웹 사이트 제작
- [ ] [🔒]() 해석하는 인공지능 제작
- [ ] [🔒]() 루머 청원 찾기

## 📑 Example
 국민청원 분석에서 나오는 예시들입니다.

### ☁️ 워드클라우드
![](https://d2mxuefqeaa7sj.cloudfront.net/s_5A66E0DE01CD75EDED299102E2F6453BEBCD300B9977BD6F9719ECE5E21E2C90_1548070137676_image.png)

### 🌐 네트워크
![](https://d2mxuefqeaa7sj.cloudfront.net/s_5A66E0DE01CD75EDED299102E2F6453BEBCD300B9977BD6F9719ECE5E21E2C90_1548073151578_image.png)

### 📉 그래프
![](https://d2mxuefqeaa7sj.cloudfront.net/s_5A66E0DE01CD75EDED299102E2F6453BEBCD300B9977BD6F9719ECE5E21E2C90_1548070226604_image.png)

### ✨ 중요키워드 갑질

#### 네트워크

![](https://d2mxuefqeaa7sj.cloudfront.net/s_5A66E0DE01CD75EDED299102E2F6453BEBCD300B9977BD6F9719ECE5E21E2C90_1548073035807_image.png)

#### 워드클라우드

![](https://d2mxuefqeaa7sj.cloudfront.net/s_6BA2A63FD25F3FE0CBB3C54FF3212310B170B7FB25E38BF989986B9924C49C1E_1546789797423_.png)


#### Top 키워드
```
{'국민': 244654,
 '말': 217367,
 '병원': 107206,
 '업체': 48050,
 '여성': 9752,
 '승무원': 8159,
 '사람': 7112,
 '갑질': 4138,
 '대한민국': 4121,
 '아이': 4027,
 '생각': 3959,
 '정부': 3764,
 '국가': 3732,
 '사건': 3520,
 '치료': 3460,
 '의사': 3374,
 '피해자': 3270}
```

#### 해석
 갑질의 경우 국민, 병원, 업체, 여성, 승무원, 치료, 의사, 피해자 등으로 병원 업체에서 의사가 치료를 가지고 갑질을 했거나 승무원이 갑질을 한 것인지 당한 것인지 그리고 어떠한 업체에서 갑질이 있었던 것으로 예상됩니다. 갑질과 직접적인 네트워크를 보면 병원, 승무원, 업체로 이 3가지 키워드에 어떠한 갑질이 있었다고 유추할 수 있습니다.

[상습폭행을 저지른 제주대학교병원 H교수를 처벌해주세요](https://www1.president.go.kr/petitions/454533)

[대한항공 조현민 전무의 갑질을 엄중 처벌해야합니다.](https://www1.president.go.kr/petitions/196894)

[대한항공 인턴제도 갑질을 고발합니다.](https://www1.president.go.kr/petitions/269098)

 그리고 실제로 위에 대기업 키워드와 같이 병원에서 교수 의사의 갑질, 조현민 전무가 하청업체들에게 한 갑질, 항공사의 승무원 인턴제도 갑질 등 위에 관련된 키워드들의 갑질이 실제로 발생했습니다. 이를 통해 네트워크, 워드클라우드, 탑 키워드 분석에 대한 중요성을 더욱 증명할 수 있다고 생각합니다. 실제로 30만 개가 넘어가는 청원을 전부 읽기에는 무리가 있으나 관심 있는 키워드를 가지고 네트워크, 워드클라우드, 탑 키워드 분석을 통해서 짧으면서 쉽게 국민들이 생각하는 문제들을 알 수 있습니다.

## 🤝 Connect
```
# github : https://github.com/newhiwoong
# email  : newhiwoong@gmail.com
```
