from flask import Flask,render_template,request,flash
from funciones.generarPassword import password_segura


app = Flask(__name__)
app.secret_key = "wiinwardiunleviosa"


@app.route('/',methods=['POST','GET'])
def generador():
    passwd = ""
    if request.method == 'POST':
        valor = request.form.get('select')
        passwd = password_segura(valor)
        flash("Seleccione la longitud del password",'warning')



    return render_template('generador.html',passwd=passwd)




if __name__ == '__main__':
    app.run(debug=True,port=8000)
    
