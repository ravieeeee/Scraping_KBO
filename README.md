robots.txt상 allowed에서 진행했습니다.

문제가 있으면 issue로 알려주세요.

## 기술스택

* web framework : Flask

* template engine : Jinja2

* deploy : PythonAnyWhere

* db : mongodb

* crawling : Selenium

## Request & Response

**Request URL**

* http://www.kbo.space/search?date={request\_date}&team={team\_name}

**Request Parameter**

date
* 20170331 ~ 20171003 (2017 시즌)

team(case insensitive)

| parameter | Full name                    |
|-----------|------------------------------|
| 두산      | Doosan Bears(두산 베어스)    |
| NC        | NC Dinos(NC 다이노스)        |
| 넥센      | Nexen Heroes(넥센 히어로즈)  |
| LG        | LG Twins(엘지 트윈스)        |
| KIA       | KIA Tigers(기아 타이거즈)    |
| SK        | SK Wyverns(SK 와이번스)      |
| 한화      | Hanwha Eagles(한화 이글스)   |
| 롯데      | Lotte Giants(롯데 자이언츠)  |
| 삼성      | Samsung Lions(삼성 라이온즈) |
| KT        | KT Wiz(KT 위즈)              |

**Response**
JSON
* date : 날짜
* team : 팀명
* manager : 감독
* coach : 코치
* pitcher : 투수
* catcher : 포수
* infielder : 내야수
* outfielder : 외야수

XML
