# Cron
![cron_but_second](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxHWwmRhMybTdEFxggPZisM_Yr2Z7JZS7Qug&s)
- 지정한 시간마다 작업을 반복실행하는 파이프라인 구성의 일부
- 리눅스에서는 초단위는 설정못함
- cron jab 등록
```shell
crontab -e
```

- 기본 문법
```vim
* * * * * /Users/m2/.../python /Users/.../0.log_generate.py
```
- * : 분 (0-59)
- * : 시 (0-23)
- * : 일 (1-31)
- * : 월 (1-12)
- * : 요일 (0-6, 0은 일요일)

- cron 리스트 확인

```shell
crontab -l
```