# 이름과 나이를 입력받아 다음과 같은 출력한다
# 홍길동님은 성년입니다 or 홍길동님은 미성년입니다
# 단 성년인 경우 글자색 파랑, 미성년인 경우 글자색 빨강
from flask import Flask, request, render_template

app=Flask(__name__)
@app.route('/work', methods=['get'])
def wokr_input():
    return render_template('/work_input1.html')

@app.route('/work', methods=['post'])
def wokr_print():
    irum = request.form.get('irum', type=str)
    nai = request.form.get('nai', type=int)
    # if나 for는 flask 또는 html에서 가능
    is_adult = nai>= 18
    return render_template('/work_result1.html', irum=irum, nai=nai, is_adult=is_adult)

# @app.route('/work1', methods=['get'])
# def wokr_input():
#     return render_template('/work_input.html')

# @app.route('/work1', methods=['post'])
# def wokr_print():
#     irum = request.form.get('irum', type=str)
#     nai = request.form.get('nai', type=int)

app.run(debug=True)