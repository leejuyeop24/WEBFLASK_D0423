### ===> 모듈로딩
from flask import Flask

### ===> 전역변수
APP = Flask(__name__)

### ===> 라우팅(Routing) 기능 함수들

@APP.route("/")
def index():
	return "<h1><font color='blue'>Hello MyWeb~!!</font></h2>"

### ===> 조건에 따른 실행 처리
if __name__ == '__main__':
	APP.run()