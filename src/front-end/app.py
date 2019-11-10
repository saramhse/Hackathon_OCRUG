from flask import Flask, render_template, redirect, url_for, request
from onehotlist import onehotnames
import pandas as pd
import pickle
import os
app = Flask(__name__)

filename = open('ocrug_finalized_model.sav','rb')
model = pickle.load(filename)

@app.route('/')
def Index():
    return redirect(url_for('Model'))

@app.route('/model')
def Model():
    return render_template('ScoreAssesment.html', active_page="model")


@app.route('/visualization')
def Visualization():
    return render_template('DataVisualization.html', active_page="visualization")

@app.route('/team')
def About():
    return render_template('Team.html', active_page="team")

# API calls
@app.route('/generateModel', methods=['POST'])
def GenerateModel():
    values = request.form.to_dict()
    df = pd.DataFrame(values, index=[0])

    df['age'] = df['age'].astype('int')
    df['balance'] = df['balance'].astype('int')
    df['month'] = df['month'].astype('int')
    df['duration'] = df['duration'].astype('int')
    df['campaign'] = df['campaign'].astype('int')
    df['previous'] = df['previous'].astype('int')

    df['day_bin'] = df['day_bin'].astype('category')
    df['pdays_bin'] = df['pdays_bin'].astype('category')

    df_onehot=pd.get_dummies(df,columns=['day_bin','pdays_bin','job','marital','education','default','housing','loan','contact','poutcome'])

    headers = onehotnames()
    for i in headers:
        if i in df_onehot.columns:
            pass
        else:
            df_onehot[i]=0

    # get=[]
    # for i in df_onehot.columns:
    #     get.append(i)
    #     print("'{}',".format(i))
    # print('='*50)
    # mod=[]
    # for i in headers:
    #     mod.append(i)
    #     print("'{}',".format(i))
    #     print(i)

    prediction = model.predict_proba(df_onehot.values)

    return render_template("ScoreAssesment.html", prediction = round(prediction[0][1],2))

if __name__ == '__main__':
    app.run()
