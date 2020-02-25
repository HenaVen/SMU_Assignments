from flask import Flask, render_template, jsonify
import pandas as pd


app = Flask(__name__)


@app.route('/listdata')
def listdata():
    df = pd.read_csv('data_3_hena/PredVarwithTickerVarTrend.csv')
    ticker = df.Ticker.tolist()
    return jsonify(ticker) 

@app.route('/')
def Home():   
    return render_template('index.html')

@app.route('/science')
def Science():
    return render_template('science.html')

@app.route('/test')
def Research():
    return render_template('test.html')

@app.route('/table2')
def Map():
    return render_template('table2.html')

@app.route('/about')
def About():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)