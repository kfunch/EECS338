from flask import Flask, render_template
from flask import request, jsonify
#from demoWeek10 import googleSearch
from demoWeek10_2 import googleSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        f1 = request.form['firstVerb']
        f1 = googleSearch(f1)
        r1 = f1[0]
        r2 = f1[1]
        r3 = f1[2]
        r4 = f1[3]
        return render_template('echo.html', r1=r1, r2=r2, r3=r3, r4=r4)
    return render_template('echo.html')

if __name__ == "__main__":
	app.run(debug=True)
	app.run()