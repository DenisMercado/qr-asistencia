from flask import Flask, redirect

app= Flask(__name__)

URL_formulario="https://docs.google.com/forms/d/e/1FAIpQLSeWv5DZUmmSywqXafeVMQvYm64iIpXcOSI5l2tTsga44yd44g/viewform?usp=header"

@app.route('/asistencia')
def asistencia ():

    return redirect(URL_formulario)


if __name__=="__main__":
    app.run(debug=True)
