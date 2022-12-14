import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from Project_app.utils import MedicalInsurence

app = Flask(__name__)

########################## Login API ######################################


# @app.route('/') 
# def hello_flask():
#     return 'Welcome to Flask'



# #########################################################################

# @app.route('/predict_charges',methods = ['POST','GET'])
# def get_insurence_charges():
#     if request.method == 'POST':
#         print("We are using POST method")
#         data = request.form
#         age = eval(data['age'])
#         sex = data['sex']
#         bmi = eval(data['bmi'])
#         children = eval(data['children'])
#         smoker = data['smoker']
#         region = data['region']

#         print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
#         med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
#         charges = med_ins.get_predicted_charges()

#         return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})

#     else:
#         print("We are using GET method")
#         age = eval(request.args.get('age'))
#         sex = request.args.get('sex')
#         bmi = eval(request.args.get('bmi'))
#         children = eval(request.args.get('children'))
#         smoker = request.args.get('smoker')
#         region = request.args.get('region')

#         print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
#         med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
#         charges = med_ins.get_predicted_charges()

#         return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})
 
################################# HTML Test ##############################################

@app.route('/') 
def main():
    return render_template('index.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']
        
        object = MedicalInsurence(age, sex, bmi,children,smoker, region)
        prediction = object.get_predicted_charges()

        return render_template("result.html", prediction = prediction)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = 8080,debug=False)