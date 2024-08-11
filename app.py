from flask import Flask, render_template
from gsheets_api import upload_sheets_data
import pandas as pd

app = Flask(__name__)



@app.route('/', methods=['GET'])
def homepage():
    upload_sheets_data() #updates form.csv
    df=pd.read_csv("form.csv")
    return render_template('home.html',column_names=df.columns.values, row_data=list(df.values.tolist()),zip=zip)

@app.route('/log', methods=['GET'])
def log():
    return render_template('log.html')

@app.route('/calendar', methods=['GET'])
def calendar():
    return render_template('calendar.html')

@app.route('/analytics', methods=['GET'])
def analytics():
    return render_template('analytics.html')

if __name__ == '__main__':
    app.run(debug=True)