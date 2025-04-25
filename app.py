from flask import Flask, redirect

app= Flask(__name__)

URL_formulario="https://docs.google.com/forms/d/1mbFEeeydMpK_gVDWsdW2rxg7usPKo0khom1ggEXEQUI/edit"

@app.route('/asistencia')
def asistencia ():

    return redirect(URL_formulario)


if __name__=="__main__":
    app.run(debug=True)
