#1 파일 셋팅
1. pip3 install -r requirements.txt 실행
2. production.py를 settings.py에 적용하기
3. Procfile, runtime.txt 작성

#2 heroku 설치 및 셋팅
1. brew tap heroku/brew && brew install heroku
2. 보안을 위한 환경변수 설정
   heroku config:set [DJANGO_SECRET_KEY]=[secretKey]
   heroku config:set [yourdbname]=[dbname]
   heroku config:set [yourdbusername]=[yourusername]
   heroku config:set [yourdbuserpassword]=[yourdbuserpassword]
3. settings.py에 환경변수 적용하기

#3 heroku 배포하기
1. heroku login
2. heroku create [yourWebsiteName]
3. git commit 처리하기
4. git push heroku master

#4 오류 헤결
1. DEBUG=TRUE로 설정하여 찾을수 있음