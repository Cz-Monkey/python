from flask import Flask, request, render_template, redirect
import model as m

app = Flask(__name__)

@app.route('/')
def list():
    guestbook = m.findall()
    return render_template('list.html', list=guestbook)


@app.route('/write', methods=['post'])
def write():
    name = request.form.get('name', type=str)
    content = request.form.get('content', type=str)
    m.save(name=name, content=content)
    return redirect('/')

@app.route('/delete', methods=['post'])
def delete():
    gno = request.form.get('gno', type=int)
    m.delete(gno=gno)
    return redirect('/')

@app.route('/update', methods=['post'])
def update():
    gno = request.form.get('gno', type=int)
    content = request.form.get('content',type=str)
    m.update(gno=gno, content=content)
    return redirect('/')

app.run(debug=True)