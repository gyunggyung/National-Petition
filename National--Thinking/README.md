# National-Petition-Government-Thinking
국민청원 글 중에 정부에서 답변을 한 글들에 대해서 분석을 합니다.

## 추천 수별로 워드클라우드 제작
추천 수별로 [워드클라우드](https://github.com/newhiwoong/National-Petition/tree/master/Word-Cloud) 그리고 추천 수별 그래프를 통한 분석을 진행합니다.

### 추천수 0개인 청원에 대한 워드클라우드
```
keyword0 = make_cloud(df[df["count"]==0],"기타", png_name="1.jpg",state="img",max_font_size_n = 100,background_color_n='black')

```

![](https://github.com/newhiwoong/National-Petition/blob/master/National--Thinking/img/0.png)

### 추천수 21~40개인 청원에 대한 워드클라우드
```
keyword5 = make_cloud(df[(df["count"]>=21) & (df["count"]<=40)],"기타", png_name="6.JPG",state="img",max_font_size_n = 100,background_color_n='black')
```

![](https://github.com/newhiwoong/National-Petition/blob/master/National--Thinking/img/21-40.png)

## 그래프 만들기 
 추천 수별로 많이 보이는 키워드들을 찾아서 그 키워드들이 월별로 얼마나 등장했는지를 확인합니다.

[그래프 제작 code](https://github.com/newhiwoong/National-Petition/blob/master/National--Thinking/graph.ipynb)


### 추천수가 100개 이상인 키워드들에 대한 그래프 제작 

```
font_name = fm.FontProperties(fname = "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf").get_name()
mpl.rc('font', family = font_name)

plt.subplots(1, figsize = (20,6))
for t_l,t_m in zip(t_100_list,t_100):
    plt.plot(months,t_l,label=t_m)
plt.grid()
#plt.legend()
plt.xlabel("Month")
plt.ylabel("Number of appearances")
plt.title("Graph 100+ suggestions every month")
plt.show()
```

![](https://github.com/newhiwoong/National-Petition/blob/master/National--Thinking/img/gp_100.png)