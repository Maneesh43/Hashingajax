from flask import Flask, render_template, request, jsonify,abort
from flask_mail import Mail, Message
import hashlib as h
#from flask_restful import Resource, Api
#from flask_httpauth import  HTTPBasicAuth
app = Flask(__name__)
mail=Mail(app)
#api = Api(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'appalerts43@gmail.com'
app.config['MAIL_PASSWORD'] = 'maneesh43'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
#class test1(Resource):
	#def get(self,id):
		#return jsonify({'result':id})
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
            if(hash1=="sha1"):newName=h.sha1(text1.encode()).hexdigest()
            elif(hash1=="blake2b"):newName=h.blake2b(text1.encode()).hexdigest()
            elif(hash1=="sha224"):newName=h.sha224(text1.encode()).hexdigest()
            elif(hash1=="shake_128"):newName=h.shake_128(text1.encode()).hexdigest()
            elif(hash1=="sha3_224"):newName=h.sha3_224(text1.encode()).hexdigest()
            elif(hash1=="sha384"):newName=h.sha384(text1.encode()).hexdigest()
            elif(hash1=="sha256"):newName=h.sha256(text1.encode()).hexdigest()
            elif(hash1=="sha3_256"):newName=h.sha3_256(text1.encode()).hexdigest()
            elif(hash1=="shake_256"):newName=h.shake_256(text1.encode()).hexdigest()
            elif(hash1=="sha1"):newName=h.sha1(text1.encode()).hexdigest()
            elif(hash1=="sha3_384"):newName=h.sha3_384(text1.encode()).hexdigest()
            elif(hash1=="blake2s"):newName=h.blake2s(text1.encode()).hexdigest()
            elif(hash1=="sha512"):newName=h.sha512(text1.encode()).hexdigest()
            elif(hash1=="md5"):newName=h.md5(text1.encode()).hexdigest()
            elif(hash1=="sha3_512"):newName=h.sha3_512(text1.encode()).hexdigest()
            else:newName="Failed to generate Hash please report it to get it debugged"
            return jsonify({'text1' : newName})
        else:
            return jsonify({'error' : 'Missing data!'})
@app.route('/encrypt')
def encrypt1():
    return render_template('misc1.html')
@app.route('/misc')
def misc1():
    return render_template('misc1.html')
@app.route('/contact')
def contactme():
    return render_template('contactm.html')
@app.route('/.well-known/brave-rewards-verification.txt')
def serve1():
    return app.send_static_file('/.well-known/brave-rewards-verification.txt')
@app.route('/sendmail',methods=['POST'])
def sendmail():
    if request.method=="POST":
        a=request.form['t1']
        b=request.form['t2']
        c=request.form['t3']
        msg = Message(subject='App alerts', sender = 'appalerts43@gmail.com', recipients = ['appalerts43@gmail.com'])
        msg.body=c
        mail.send(msg)
        a="sent"
        if(a=="sent"):return jsonify({'text1' : a})
        else:return jsonify({'error' : 'Failed to send message'})
    else:return "Unsupported method used"
#api.add_resource(test1,'/test/<id>')
@app.errorhandler(404)
def error404(e):
        return "A unknown error has occured",0
@app.route('/api',methods=['GET'])
def apir():
            if request.method=="GET":
                    a=request.args.get("user")
                    b=request.args.get("pass")
                    if a=="maneesh" and b=="123":
                        return "success"
                    else: return "failure"
            else: "wrong request"
if __name__ == '__main__':
	app.run(debug=True)
