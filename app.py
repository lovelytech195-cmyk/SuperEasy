from flask import Flask,render_template
import json
import os
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
    port =int(os.environ.get('PORT', 5000))
    app.run(debug = True, host='0.0.0.0', port=port)
