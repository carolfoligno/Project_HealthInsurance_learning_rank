# teste da minha api

import os
import pickle5 as pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

# loading model
# carrega na memoria direto, torna o request para predição mais rápido
model = pickle.load(open('web_app/models/model_rf.pkl', 'rb'))

# deixar modelo salvo em banco de memoria como:
# RabbitMQ e Redis

# initialize API
app = Flask(__name__)

@app.route('/predict', methods=['POST']) # recebe apenas requisição
def health_insurance_predict():
    
    test_json = request.get_json()
    
    if test_json: # tem dados
        if isinstance(test_json, dict): # unico linha
            test_raw = pd.DataFrame(test_json, index=[0])
            
        else: #multiple linhas
            test_raw = pd.DataFrame(test_json, columns= test_json[0].keys())
            
        # instantiate 
        pipeline = HealthInsurance()
        
        # data clening
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
        
    else:
        return Response('{}', status=200, minetype='application/json')
    
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host= '0.0.0.0', port=port)