from flask import Flask, request, render_template, redirect
import dao

app = Flask(__name__)

@app.route('/')
def list():
    gb = dao.findall()
    return render_template('list.html',list=gb)

@app.route('/read')

@app.route('/write')

@app.route('/write', methods=['post'])
def save():
    title = request.form.get('title', type=str)
    writer = request.form.get('writer', type=str)
    ingi = request.form.get('ingi', type=int)
    content = request.form.get('content', type=str)
    dao.save(title=title, writer=writer, ingi=ingi, content=content)
    return redirect('/')
    

@app.route('/delete', methods=['post'])
def delete():
    gno = request.form.get('gno', type=int)
    dao.delete(gno)
    return redirect('/')

app.run(debug=True)