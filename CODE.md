<h1 align="center">  National-Petition </h1>
<div align="center">

![COM LAB LOGO](https://d2mxuefqeaa7sj.cloudfront.net/s_6BA2A63FD25F3FE0CBB3C54FF3212310B170B7FB25E38BF989986B9924C49C1E_1546608400699_13.png)

국민청원 사이트 분석에 설정과 코드에 대한 간단한 설명을 진행합니다.

</div>
## Petition Data
국민청원을 분석하기 위해 국민청원 사이트를 [크롤링한 데이터](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)를 다운로드합니다.

## Install files
 기본적으로 [Git](https://git-scm.com/)은 설치되있다고 가정하겠습니다. 국민청원 분석을 하는 코드를 저장할 하위 폴터에서 아래 코드를 실행시킵니다.

```
git init
git clone https://github.com/newhiwoong/National-Petition.git
```

 그럼 `National-Petition` 폴터가 생성될 것입니다. 이제 [국민청원 Data](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)를 `National-Petition` 폴더 내부에 넣습니다.

## Required package
기본적으로 [ANACONDA](https://www.anaconda.com/download/) 환경에 [jupyter notebook](https://jupyter.org/)에서 진행합니다. 이를 위해 [ANACONDA](https://www.anaconda.com/download/) 설치 및 환경 설정이 필수적으로 필요합니다.

그리고 주로 [KoNLPy](http://konlpy.org/en/latest/)를 많이 사용하는데 이를 위해 [Java](https://www.java.com/ko/download/) 설치 및 환경설정이 필요합니다. 

이후 필요한 내용은 [Installation Code](https://github.com/newhiwoong/National-Petition/blob/master/installation_code.ipynb)를 실행하시면 필요한 Package들이 설치됩니다.

## CODE
청원 분석에 대해 제작할 코드들입니다.

### Todo list

- [x] 국민청원 게시판 크롤링 [CODE](https://github.com/newhiwoong/National-Petition/tree/master/Data)
- [x] 국민청원 게시판 분석 내용 [DOCS](https://github.com/newhiwoong/National-Petition)
- [ ] 영어 키워드 찾기 
