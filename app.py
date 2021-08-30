import pickle
import numpy
from flask import Flask, request, render_template

app = Flask(__name__)
loadedmodel = pickle.load(open('loan_data_set.pkl','rb'))

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html')
@app.route("/prediction", methods =['POST'])
def predict():
    Total_Income = int(request.form['Total_Income'])
    LoanAmount = int(request.form['LoanAmount'])
    LoanAmountTerm = int(request.form['LoanAmountTerm'])
    CreditHistory = int(request.form['CreditHistory'])

    prediction = loadedmodel.predict([[Total_Income,LoanAmount,LoanAmountTerm,CreditHistory]])
    if prediction == [0]:
        prediction = 'Sorry Your loan will not get approved.'
    else:
        prediction = 'Yay! Your loan will be approved.'
    return render_template('index.html', output = prediction )
#main function
if __name__ == "__main__":
    app.run(debug=True)
