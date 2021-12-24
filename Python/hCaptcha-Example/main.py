# 직접 해본 hCaptcha 예제

from flask import Flask, render_template, request
from flask_hcaptcha import hCaptcha

##########################################################

app = Flask(__name__)
app.config['HCAPTCHA_ENABLED'] = True # BOOL
app.config['HCAPTCHA_SITE_KEY'] = "" # SITE KEY
app.config['HCAPTCHA_SECRET_KEY'] = "" # SECRET KEY
hcaptcha = hCaptcha(app)

host = '0.0.0.0'
port = '8080'
debug = True

##########################################################

"""
이제 index.html 쪽에 POST로 '{{ hcaptcha }}' 라고 넣으시면 됩니다.
당연히 /check로 이동하게요.
"""

@app.route('/')
def index():
  return render_template('index.html') # index는 대충 이렇게

@app.route('/check', methods = ['POST'])
def check():
    if hcaptcha.verify():
        return "성공"
    else:
        return "실패"
      
##########################################################
        
app.run(host = host, port = port, debug=debug)
