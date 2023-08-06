from flask import Flask, render_template,request
import pickle
import sklearn
import numpy as np
model=pickle.load(open('model1.pkl','rb'))
app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index1.html")

@app.route('/predict',methods=['POST'])
def predict_placement():
    height=float(request.form.get('height'))
    weight= float(request.form.get('weight'))
    result=model.predict(np.array([height,weight]).reshape(1,2))
    if result[0]==1:
        result ="You are a MAN"
    else:
        result ="You are a WOMAN"
    return render_template('index1.html',result=result)
if __name__=='__main__':
    app.run(debug=True)