from flask import Flask, redirect

app= Flask(__name__)

URL_formulario="https://docs.google.com/forms/d/e/1FAIpQLSd_BjAFrGLae9yZQ6RdUUKB0tF1ZiL9MqJvB5wpnoqTEbryDA/viewform"

@app.route('/asistencia')
def asistencia ():

    return redirect(URL_formulario)


if __name__=="__main__":
    app.run(debug=True)
