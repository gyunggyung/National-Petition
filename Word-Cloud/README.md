# National-Petition-Word-Cloud
국민청원 내용의 분류별 그리고 월별 워드클라우드를 진행합니다.


## 글꼴 설정

```
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

```
font_path="/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
```

이 2개 부분을 자신의 한글 폰트경로로 바꿔주셔야합니다~

```
/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf
```

mac : https://pinkwink.kr/990

## 예시

