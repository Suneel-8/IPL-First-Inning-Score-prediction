from flask import Flask,render_template,request
import numpy as np
import pickle
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

regressor=pickle.load(open('model.pkl','rb'))
@app.route('/predict' , methods=['POST'])
def predict():
    #for rendering results on html GUI
    if request.method=='POST':
        batting_team = request.form['bating-team']
        if batting_team == 'Chennai Super Kings':
            batting = [1, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Delhi Capitals':
            batting = [0, 1, 0, 0, 0, 0, 0]
        elif batting_team == 'Kings XI Punjab':
            batting = [1, 0, 1, 0, 0, 0, 0]
        elif batting_team == 'Kolkata Knight Riders':
            batting = [0, 0, 0, 1, 0, 0, 0]
        elif batting_team == 'Mumbai Indians':
            batting = [0, 0, 0, 0, 1, 0, 0]
        elif batting_team == 'Rajasthan Royals':
            batting = [0, 0, 0, 0, 0, 1, 0]
        elif batting_team == 'Royal Challengers Bangalore':
            batting = [0, 0, 0, 0, 0, 0, 1]
        elif batting_team == 'Sunrisers Hyderabad':
            batting = [0, 0, 0, 0, 0, 0, 0]

        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            bowling = [1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Delhi Capitals':
            bowling = [0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kings XI Punjab':
            bowling = [1, 0, 1, 0, 0, 0, 0]
        elif bowling_team == 'Kolkata Knight Riders':
            bowling = [0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == 'Mumbai Indians':
            bowling = [0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == 'Rajasthan Royals':
            bowling = [0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == 'Royal Challengers Bangalore':
            bowling = [0, 0, 0, 0, 0, 0, 1]
        elif bowling_team == 'Sunrisers Hyderabad':
            bowling = [0, 0, 0, 0, 0, 0, 0]
        overs = float(request.form['over'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        wickets_last_5 = int(request.form['wickets_last_5'])

        x = np.array(batting + bowling + [runs, wickets, overs, wickets_last_5])
        x = x.reshape(1, -1)
        predicted_run = int(regressor.predict(x))
        return render_template('result.html' , lower_limit=predicted_run-10,upper_limit=predicted_run+5)


if __name__ == '__main__':
    app.run(debug=True)
#debug=True
