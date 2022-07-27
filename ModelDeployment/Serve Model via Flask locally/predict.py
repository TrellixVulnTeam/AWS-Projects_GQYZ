from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
model = pickle.load(open('/home/ec2-user/notebooks/models/model','rb'))

def predictc(features):
    print("Inside predictc")
    predictions = model.predict(features)
    print(predictions)
    return predictions[0]
app = Flask('app')

@app.route('/predict',methods=['POST'])
def predict_endpoint():
    features = request.get_json()
    print("Inside predict_endpoint")
    print(features)
    feature_df = pd.DataFrame.from_dict([features])
    
    predictions = predictc(feature_df)
    print(predictions)
    
    result = {
        'Class' : str(predictions)
    }
    print(result)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9697)
