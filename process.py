from flask import Flask, render_template, request, jsonify
import hashlib as h
app = Flask(__name__)
@app.route('/')
def index():
    a=h.algorithms_guaranteed
    b=list(a)
    c={b[i]:i for i in range(0,len(b))}
    return render_template('form.html',a1=c)
@app.route('/process', methods=['POST'])
def process():
        text1 = request.form['text1']
        hash1 = request.form['hash1']
        if text1 and hash1:
            newName = h.md5(text1.encode()).hexdigest()
            return jsonify({'text1' : newName})
        else:
            return jsonify({'error' : 'Missing data!'})
if __name__ == '__main__':
	app.run(debug=True)
