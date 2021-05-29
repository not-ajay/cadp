import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app=Flask(__name__,template_folder='template')
model = pickle.load(open('mo.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('home.html')

#To use the predict button in our web-app
@app.route("/predict")
def predict():
    return render_template('predict.html')

@app.route('/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction==1:
       return render_template('yes.html')
    else:
       return render_template('no.html')


@app.route("/symptoms")
def symptoms():
  return render_template("symptoms.html")

@app.route("/TEST")
def TEST():
  return render_template("TEST.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)