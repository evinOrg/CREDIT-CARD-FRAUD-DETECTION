import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

def app():
    xgb_model = joblib.load('xgb_model.pkl')
    catboost_model = joblib.load('catboost_model.pkl')
    def predict(model, data):
        prediction = model.predict(data)
        return prediction
    def encode_categorical(df):
        le = LabelEncoder()
        categorical_cols = ['merchant', 'category', 'job']
        for col in categorical_cols:
            df[col] = le.fit_transform(df[col])
        return df

    st.header('Enter Transaction Details')
    df = pd.read_csv('fraud.csv')
    search_cc_num = st.number_input('Credit Card No')
    result = df[df['cc_num'] == float(search_cc_num)]  
    columns_to_print = ['trans_date_trans_time', 'merchant', 'category', 'amt', 'first', 'last','unix_time']
    unix_times = result['unix_time'].drop_duplicates()
    selected_unix_time = st.selectbox('Select a Unix time', unix_times)
    corresponding_row = df[df['unix_time'] == selected_unix_time]
    if not corresponding_row.empty:
        search_cc_num = corresponding_row['cc_num'].values[0]
        merchant =  st.text_input('Merchant', value=corresponding_row['merchant'].values[0])
        category = st.text_input('Category', value=corresponding_row['category'].values[0])
        amt = st.number_input('Amount', value=corresponding_row['amt'].values[0])
        gender = st.selectbox('Gender', ['M', 'F'], index=0 if corresponding_row['gender'].values[0] == 'M' else 1)
        lat = st.number_input('Latitude', value=corresponding_row['lat'].values[0])
        long = st.number_input('Longitude', value=corresponding_row['long'].values[0])
        city_pop = st.number_input('City Population', value=corresponding_row['city_pop'].values[0])
        job = st.text_input('Job', value=corresponding_row['job'].values[0])
        unix_time = corresponding_row['unix_time'].values[0]
        merch_lat = st.number_input('Merchant Latitude', value=corresponding_row['merch_lat'].values[0])
        merch_long = st.number_input('Merchant Longitude', value=corresponding_row['merch_long'].values[0])
    else:
        st.write("No data found")
    if st.button('Predict'):
        data = [[merchant, category, amt, 1 if gender == 'M' else 0, lat, long, city_pop, job, unix_time, merch_lat, merch_long]]
        df = pd.DataFrame(data, columns=['merchant', 'category', 'amt', 'gender', 'lat', 'long', 'city_pop', 'job', 'unix_time', 'merch_lat', 'merch_long'])
        df = encode_categorical(df)
        predict(catboost_model, df)
        xgb_prediction = xgb_model.predict(df)
        catboost_prediction =catboost_model.predict(df)
        st.subheader('XGBoost Model Prediction:')
        st.write('Fraudulent' if xgb_prediction == 1 else 'Legitimate')
        st.subheader('CatBoost Model Prediction:')
        st.write('Fraudulent' if catboost_prediction == 1 else 'Legitimate')
