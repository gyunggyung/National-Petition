# National-Petition-Government-Thinking
국민청원 글 중에 정부에서 답변을 한 글들에 대해서 분석을 합니다.

## 데이터 분석
 답변한 글들의 분류와 월을 확인합니다. 
 
 먼저 브리핑 즉, 정부가 답변을 한 청원들로 필터링을 진행합니다. 
```
df = df[df["progress"]=="브리핑 "]
df
```

 [데이터 분석](https://github.com/newhiwoong/National-Petition/tree/master/National--Thinking)에서와 같이 분야별 데이터 수를 확인합니다.

```
i= 0
fied_names_num(df[df["count"]>=i],names)
```

### 분야별 브리핑 수 
```
보건복지  :  3
반려동물  :  3
육아/교육  :  2
기타  :  7
인권/성평등  :  21
안전/환경  :  8
성장동력  :  2
미래  :  1
교통/건축/국토  :  2
문화/예술/체육/언론  :  7
행정  :  1
정치개혁  :  5
외교/통일/국방  :  4
경제민주화  :  2
all :  68
```

### 월별 브리핑 수 
```
2017-09  :  3
2017-11  :  3
2017-12  :  2
2018-01  :  7
2018-02  :  7
2018-03  :  6
2018-04  :  5
2018-05  :  8
2018-06  :  7
2018-07  :  3
2018-09  :  2
2018-10  :  12
2018-11  :  3
all :  68
```

## 워드클라우드
[워드클라우드](https://github.com/newhiwoong/National-Petition/tree/master/Word-Cloud)에서와 같이 워드클라우드를 진행합니다.


### 국민의 청원들로 워드클라우드
국민의 청원들만 가지고 워드클라우드를 진행합니다. 
```
def make_cloud(category, png_name=0,state="no", background_color_n='white', max_font_size_n = 40):
    text = list(df["petition_overview"])
    text = ' '.join(text)
    
    ko_con_text = text
    print(len(text))
    #print(text)
    tokens_ko = t.nouns(ko_con_text)
    print("ok")
    stop_words = ['직','제','저', '이','그','때','및','것이','합니다.','\\n',':','','거','수','그' ,"합","이","있는","있습니다.","것","및","하지만","때문에"]
    tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]

    text = ' '.join(tokens_ko)
    ....
```
```
keyword = make_cloud("기타", png_name="tr.JPG",state="img",max_font_size_n = 100,background_color_n='black')0
```

![청원 키워드](https://d2mxuefqeaa7sj.cloudfront.net/s_6BA2A63FD25F3FE0CBB3C54FF3212310B170B7FB25E38BF989986B9924C49C1E_1546599419684_tr1.png)

### 답변을 가지고 워드클라우드를 진행합니다.
답변을 가지고 워드클라우드를 진행합니다.  
```
def G_make_cloud(category, png_name=0,state="no", background_color_n='white', max_font_size_n = 40):
    text = list(df["petition_answer"])
    text = ' '.join(text)
    ....
```

```
keyword = G_make_cloud("기타", png_name="tr2.JPG",state="img",max_font_size_n = 100,background_color_n='black')
```

![답변 키워드](https://d2mxuefqeaa7sj.cloudfront.net/s_6BA2A63FD25F3FE0CBB3C54FF3212310B170B7FB25E38BF989986B9924C49C1E_1546703939804_ga.png)

