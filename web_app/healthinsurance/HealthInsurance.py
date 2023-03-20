import pickle 
import numpy as np
import pandas as pd

class HealthInsurance:
    
    def __init__(self):
        # variável de classe
        self.home_path = '' 
        # caminho relativo, em produção tira esse caminho
        
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler = pickle.load(open(self.home_path + 'features/age_scaler.pkl', 'rb'))
        self.vintage_scaler = pickle.load(open(self.home_path + 'features/vintage_scaler.pkl','rb'))
        self.target_encode_gender = pickle.load(open(self.home_path + 'features/target_encode_gender.pkl','rb'))
        self.target_encode_region = pickle.load(open(self.home_path + 'features/target_encode_region.pkl','rb'))
        self.fe_policy_sales_channel = pickle.load(open(self.home_path + 'features/fe_policy_sales_channel.pkl','rb'))
        
        
    def data_cleaning(self, df_raw):
        
        colunas = df_raw.columns

        new_cols = [i.lower() for i in colunas]

        df_raw.columns = new_cols
        
        return df_raw
    
    def feature_engineering(self, df1):
        # transformando as colunas region_code e policy_Sales_channel no tipo de variavel inteiro

        df1['region_code'] = df1['region_code'].astype(int)
        df1['policy_sales_channel'] = df1['policy_sales_channel'].astype(int)
        
        df1['age_group'] = df1.apply(lambda x: 'young' if x['age'] < 25 else
                            'adult' if x['age'] < 45 else
                             'old_adult' if x['age'] < 60 else
                            'old', axis = 1)
        
        return df1
    
    def data_preparation(self, df4):
        
        ### Standardization
        
        # 'annual_premium'
        # não faz fit_transform, pois ja vai vim com os parametros q eu já calculei no treinamento
        df4['annual_premium'] = self.annual_premium_scaler.transform(df4[['annual_premium']].values)

        ### Rescaling

        # 'age'
        df4['age'] = self.age_scaler.transform(df4[['age']].values)

        # 'vintage'
        df4['vintage'] = self.vintage_scaler.transform(df4[['vintage']].values)


        ### Encoder
        
        # 'gender'
    
        df4['gender'] = self.target_encode_gender.transform(df4['gender'], df4['response'])


        # 'region_code' - Frenquency Enconding / Target Enconding / weighted target econding
        df4['region_code'] = df4['region_code'].astype(str)
        df4['region_code'] = self.target_encode_region.transform(df4['region_code'], df4['response']) 


        # 'vehicle_age' - One Hot Enconding 
        df4 = pd.get_dummies(df4, prefix='vehicle_age', columns=['vehicle_age'])


        # 'policy_sales_channel' - Frenquency Enconding / Target Enconding
        df4['policy_sales_channel'] = df4['policy_sales_channel'].map(self.fe_policy_sales_channel)
        
        
        df4.loc[:,'policy_sales_channel'] = df4['policy_sales_channel'].map(self.fe_policy_sales_channel)
        
        damage_dict = {'No': 0, 'Yes': 1}
        df4['vehicle_damage'] = df4['vehicle_damage'].map(damage_dict)
        
        age_group_dict = {'young': 0, 'adult': 1, 'old_adult': 2, 'old': 3}
        df4['age_group'] = df4['age_group'].map(age_group_dict)

        df4 = df4.fillna(0)

        
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 
                 'policy_sales_channel', 'previously_insured']
        
        return df4[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        
        # model prediction
        # dataset já preparado para o modelo
        pred = model.predict_proba(test_data)
        
        #join prediction into original data
        original_data['score'] = pred[:,1].tolist()
        
        return original_data.to_json(orient='records', date_format='iso')