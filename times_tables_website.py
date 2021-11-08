from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    form = '''
    <html>
    <form action ="/next" method="get">
    <label for="times_table">What times table do you want?</label><br>
    <input type="text" id="times_table" name="times_table"><br>
    <input type="submit" value="Submit">
    </form>
    </html>
    '''
    return form

@app.route('/next') #Answers requests to the "/next" route
def next_row():
    times_table = request.args.get('times_table') #"request" was brought in from a flask import, lets us get query string variables
    times_table = int(times_table)
    multiplier = request.args.get('multiplier')
    answer = request.args.get('answer')
    if multiplier == None:
        multiplier = 1
        judgement = ''
    else:
        multiplier = int(multiplier)
        if int(answer) == (times_table * multiplier):
            judgement = '<label>You got it right!</label><br><br>'
        else:
            judgement = '<label> You need to practice!!!!!</label><br><br>'
        multiplier +=1
    form = f'''
    <html>
    <form method="get">
    {judgement}
    <input type="hidden" id="times_table" name="times_table" value="{times_table}">
    <input type="hidden" id="multiplier" name="multiplier" value="{multiplier}">
    <label for="answer">What is {times_table} x {multiplier}</label><br>
    <input type="text" id="answer" name="answer"><br>
    <input type="submit" value="Submit">
    </form>
    </html>
    '''
    return form

app.run(host='0.0.0.0', port=80)



