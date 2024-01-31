from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    numero_respuesta = 0
    if request.method =='POST':
        posible_numero = request.form['posible_numero']
        numero_respuesta = int(posible_numero) 

    return render_template('index.html',numero_respuesta=numero_respuesta)

app.run(debug=True)