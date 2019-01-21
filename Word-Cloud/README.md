# National-Petition-Word-Cloud
국민청원 내용의 분류별 그리고 월별 워드클라우드를 진행합니다.

[분야별 워드클라우드 제작](https://github.com/newhiwoong/National-Petition/blob/master/Word-Cloud/Word_Cloud.ipynb)

[월별 워드클라우드 제작](https://github.com/newhiwoong/National-Petition/blob/master/Word-Cloud/Word_Cloud_month.ipynb)

## 환경 설정

### 페키지 설치

먼저 konlpy 사용을 위해서 자바 설치와 환경설정이 필요합니다.

ubuntu
``` python
sudo apt install openjdk-8-jdk
```

아래 명령어로 필요한 페키지를 설치합니다.
``` python
!pip install nltk
!pip install konlpy
!pip install wordcloud
```

### 글꼴 설정

matplotlib의 경우 한글이 깨지는 현상이 발생합니다. 따라서 한글 글골 설정이 필요합니다.

``` python
    font_name = font_manager.FontProperties(fname="/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf").get_name()
    rc('font', family=font_name)
    %matplotlib inline

    data = ko.vocab().most_common(500)
    tmp_data = dict(data)

    if(png_name):
        korea = np.array(Image.open("img/"+png_name))
    else:
        korea = np.array(Image.open("img/"+category+"1.png"))
    image_colors = ImageColorGenerator(korea)

    wordcloud = WordCloud(font_path="/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
                         relative_scaling = 0.2, mask=korea,
                         background_color='white',
                          min_font_size=1, max_font_size=40
                         ).generate_from_frequencies(tmp_data)
    plt.figure(figsize=(30,30))

```

위에서

``` python
font_path="/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
```

이 2개 부분을 자신의 한글 폰트경로로 바꿔주셔야합니다.

``` python
/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf
```

mac에서 하는 방법 : https://pinkwink.kr/990

## 예시
원하는 부분에 대해서 워드클라우드를 진행합니다.

``` python
make_cloud("농산어촌")
```

![](https://github.com/newhiwoong/National-Petition/blob/master/Word-Cloud/img/%EB%86%8D%EC%82%B0%EC%96%B4%EC%B4%8C.png)

