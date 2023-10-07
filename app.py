from flask import Flask, flash, render_template, redirect, url_for, request, session
 
requerimientoHora=10
requerimientoLumenes=100
app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
ruta='/usuario'

@app.route('/')
def inicio():
    return render_template('index.html', requerimientoHora=requerimientoHora,requerimientoLumenes=requerimientoLumenes)

@app.route('/editarHora', methods=['POST'])
def editarHora():
    global requerimientoHora
    nuevo_requerimientohora = request.form.get('nuevo_requerimiento_hora')
    requerimientoHora = nuevo_requerimientohora
    return redirect(url_for('inicio'))

@app.route('/editarLumenes', methods=['POST'])
def editarLumenes():
    global requerimientoLumenes
    nuevo_requerimientolumenes = request.form.get('nuevo_requerimiento_lumenes')
    requerimientoLumenes = nuevo_requerimientolumenes
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
