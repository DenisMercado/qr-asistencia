from flask import Flask, redirect

app= Flask(__name__)

URL_formulario="https://forms.gle/ZyhbDzRxX5LggFhG6"

@app.route('/asistencia')
def asistencia ():

    return redirect(URL_formulario)


if __name__=="__main__":
    app.run(debug=True)
