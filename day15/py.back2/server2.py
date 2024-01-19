from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/im', methods=['get'])
def info_input():
    return render_template('im_input.html')

@app.route('/im', methods=['post'])
def info_print():
    irum = request.form['irum']
    live_city = request.form['live_city']
    return render_template('im_result.html', irum=irum, live_city=live_city)

app.run(debug=True)