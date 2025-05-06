# 파일명은 app.py로 고정
# 실행파일 명이 app.py가 아닐 경우 : set FLASK_APP = my_app.py  코드 입력

# 모듈로딩
from flask import Flask           # 클래스 호출

# 전역변수
APP = Flask(__name__)
APP.config['debug'] = 'True'

# (1) 라우팅 기능 함수들 : URL에 따른 처리 화면 설정 함수들
# 기본 : http://127.0.0.1:5000
@APP.route("/") # /는 기본 URL을 의미
def index():
    return """<h1><font color='red'>Tung Tung Tung Tung Tung Tung Tung Tung Tung Sahur</font></h2>
            <img src="/static/sahur.jpg" alt="Tung Image" width="300">"""


# (2) 링크 타고 들어가기 
# 기본에다가 hello가 붙음 : http://127.0.0.1:5000/hello
@APP.route("/hello") 
def hello():
    return "Request URL : /hello"


# (3) 변수 URL
# 기본에다가 자체 입력한 문자열이 붙음 : http://127.0.0.1:5000/<msg>
@APP.route("/<msg>") 
def message(msg):
    return f"변수 URL : /{msg}"

@APP.route("/<int:num>") 
def repeat(num):
    return f"변수 URL : {'abc' * num}"
            

# (4) 리다이렉트 URL
# 다시 처음 URL로 연결되게 하기 
@APP.route("/userinfo") 		## http://127.0.0.1:5000/userinfo
def userinfo():
    # return App.redirect('/')
    return APP.redirect('/')

@APP.route("/home/") 		## http://127.0.0.1:5000/home/
def home():
    return APP.redirect('/')



# 조건에 따른 실행처리
if __name__ == '__main__':
    APP.run()     # Flask 웹 서버 구동 
