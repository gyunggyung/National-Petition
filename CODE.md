<h1>  National-Petition </h1>

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
  |  |-images                              #필요한 이미지들
  |  |  |-.jpg                             #여러 사진 파일들
  |  |-Create_a_graph.ipynb                #그래프를 만드는 코드
  |....
  |-CODE.md                                #코드를 설명하는 md파일 (추후 README로 바꿀 예정)
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

- [x] 국민청원 게시판 분석 내용 [DOCS](https://github.com/newhiwoong/National-Petition)
- [x] 국민청원 게시판 크롤링 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Data)
- [ ] 영어 키워드 찾기 
