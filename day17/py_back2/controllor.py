from flask import Flask, request, render_template, redirect
import dao

app = Flask(__name__)

@app.route('/')
def list():
    gb = dao.findall()
    return render_template('list.html',list=gb)

@app.route('/read')
def 읽기():
    gno = request.args.get('gno', type=int)
    board = dao.findone(gno)
    return render_template('read.html', board=board)

@app.route('/write')
def 쓰기화면():
    return render_template('write.html')


@app.route('/write1', methods=['post'])
def save():
    title = request.form.get('title', type=str)
    writer = request.form.get('writer', type=str)
    content = request.form.get('content', type=str)
    dao.save(title=title, writer=writer, content=content)
    return redirect('/')
    

@app.route('/delete', methods=['post'])
def delete():
    gno = request.form.get('gno', type=int)
    dao.delete(gno)
    return redirect('/')

app.run(debug=True)