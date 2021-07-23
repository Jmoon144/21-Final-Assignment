# 21-Final-Assignment
# 아파트 관리비 시스템 보고서 API
## 프로젝트 소개

1. 관리자는 세대별 관리비를 확인할 수 있습니다. (관리사무소용 API)
    - 관리용 비밀번호 혹은 인증을 통과해야만 이 API에 접근할 수 있습니다.
  
2. 각 세대별로 자신의 관리비를 확인할 수 있습니다. (세대별 관리비 API)
    - 세대 비밀번호 혹은 인증을 통과해야만 이 API에 접근할 수 있습니다.



-----------------------

## 실행방법
1. 
```
https://github.com/Jmoon144/21-Final-Assignment.git
```

2. manage.py 가 있는 위치에서
```
docker-compose up #실행
```

3. admin user 생성

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/81899770/126758723-2c09aa3b-69eb-4f4a-853b-92d4fe04119e.gif)

4. public post를 통한 데이터 확인


![ezgif com-gif-maker (6)](https://user-images.githubusercontent.com/81899770/126759335-faf7889b-fddb-4be9-a3e7-9cb4b6567ab9.gif)

5. admin 페이지에서 관리자 로그인 후 public 리스트 확인 


![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/81899770/126759543-e3c90ffa-de85-4760-8376-8bd372fa927a.gif)


------------------------

## Folder Structure

```
├────── api
│   ├── admins
│   ├── publics  
│   └── urls.py
│
├────── docker-compose.yml
├────── fa
├── manage.py
├── my_settings.py
├── requirements.txt
```


-----------------------
## REST API


|Web API             |URL                 |Description|
|--------------------|--------------------|     -     |
|admin register      |/api/admin/user/    |     -     |
|public              |/api/public         |     -     |
|public list         |/api/admin          |     -     |



---------------------------

## Database

mysql use as Database.


