from flask import Flask,render_template
import json
with open ('quizz.json','r') as f:
    quiz_data = json.load(f)
    'data=quiz_data'
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('l.html')


@app.route('/users')
def result():
    with open('quizz.json','r') as f:
         quiz_data = json.load(f)
         'data=quiz_data'
    
    return render_template('quiz.html',data=quiz_data)
if __name__ == '__main__': 
    app.run(debug = True, host='127.0.0.1', port=5000)
