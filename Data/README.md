# National-Petition-Crawler

청원 정보를 크롤링합니다.

## Data
[petition_data_all.csv](https://www.dropbox.com/s/4q5neb9ngdhfg8y/petition_data_all.csv?dl=0)

## Crawler
[code]()

 국민청원 데이터를 분석하기 위해 먼저 크롤링을 진행합니다.

### 일반 크롤링
```
csvFile = open("petition1.csv", 'w', encoding='UTF-8')
writer = csv.writer(csvFile)
writer.writerow(["num","category","start-days","end-days","person","progress","title","count","petition_overview"])
for i in range(21,484869): #여기가 몇 개부터 몇 개까지 크롤링할지 결정
    FindPetition(i)
csvFile.close()
```

### 멀티코어 크롤링
```
csvFile = open("petition.csv", 'w', encoding='UTF-8')
writer = csv.writer(csvFile)
writer.writerow(["num","category","start-days","end-days","person","progress","title","count","petition_overview"])
csvFile.close()

csvFile = open("petition.csv", 'a', encoding='UTF-8')
writer = csv.writer(csvFile)
nums = [i for i in range(21,484869)] #크롤링 
pool = Pool(processes=4) #프로세스 숫자 쓰기
pool.map(FindPetition,nums)
csvFile.close()
```
으로 크롤링을 진행합니다.

## Filtering
[code]()

 필터링을 하기 전에 count 즉 참여인원은 int형이 아닌 문자로 이뤄져 있습니다. 이를 몇 명이 참여를 했는지 알아보기 위해서 필터링을 진행합니다.

```
def find_int(count):
    i = (re.findall(r'\d+', count))
    ints = int(''.join(map(str, i)))
    return ints
```
 아래와 같이 map 함수를 사용해서 int형으로 변환시킵니다.
```
df["count"] = df["count"].map(find_int)
df
```