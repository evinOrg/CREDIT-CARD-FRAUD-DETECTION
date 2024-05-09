import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import plotly.express as px
@st.cache_data
def app():
    train = pd.read_csv('Train.csv')
    test = pd.read_csv('Test.csv')
    df = pd.concat([train, test], ignore_index=True)
    st.header('No of Rows and Columns in Dataset')
    st.write("<span style='color:red; font-weight:bold; font-family:Arial, sans-serif;'>Shape: {}</span>".format(df.shape), unsafe_allow_html=True)
    st.header('Dataset')
    df_display = df.head().reset_index(drop=True).drop(columns=['Unnamed: 0'], errors='ignore')
    st.write(df_display)
    st.header('Fraudulent Transactions Distribution')
    st.write('0 - not fraud and 1- fraud')
    fraud_counts = df['is_fraud'].value_counts()
    st.write(fraud_counts)
    labels = ['Not Fraudulent', 'Fraudulent']
    values = fraud_counts.values
    st.plotly_chart(px.pie(values=values, names=labels, title='Fraudulent Transactions Distribution').update_traces(textposition='inside', textinfo='percent+label'))
    st.header('Looking into columns and cleaning')
    def clean_df(df):
        return df.drop(['first', 'last', 'street', 'city', 'state', 'zip', 'dob', 'trans_num','trans_date_trans_time'],axis=1)
    df = clean_df(df)
    st.header('After cleaning the columns')
    df_display = df.head().reset_index(drop=True).drop(columns=['Unnamed: 0'], errors='ignore')
    st.write(df_display)
    st.header('Attribute used in Model')
    # Display attributes one by one
    st.write("Number of Non-Null values:")
    st.write(df.info(verbose=False, memory_usage=False))
    st.write("Data Types:")
    st.write(df.dtypes)

    st.header('Splitting data into train and test')
    train1, test2 = train_test_split(df, test_size=0.2, shuffle=True, random_state=42)
    train1 = train1.reset_index(drop=True)
    test2 = test2.reset_index(drop=True)
    st.header('Data used for Train')
    st.write("<span style='color:red; font-weight:bold; font-family:Arial, sans-serif;'> {}</span>".format(train1.shape), unsafe_allow_html=True)
    st.header('Data used for Test')
    st.write("<span style='color:red; font-weight:bold; font-family:Arial, sans-serif;'> {}</span>".format(test2.shape),unsafe_allow_html=True)
    st.header('Data Visualization')
    
    df["is_fraud_cat"] = df.is_fraud.apply(lambda x: "T" if x == 1 else "F")

    # Creating the Streamlit app
    

    # Number of Credit Card Frauds by Category
    
   
    def scatter_plot(data):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(data['amt'], data['city_pop'])
        ax.set_title('Amount vs City Population')
        ax.set_xlabel('Amount')
        ax.set_ylabel('City Population')
        st.pyplot(fig)

# Display scatter plot
    scatter_plot(train)
   
    
    fig1 = px.bar(df[df['is_fraud_cat'] == "T"].groupby('category').size().reset_index(name='count'), 
                x='category', y='count', 
                title="Number of Credit Card Frauds by Category")
    st.plotly_chart(fig1)

    # Number of Credit Card Frauds by Gender
    
    fig2 = px.bar(df[df['is_fraud_cat'] == "T"].groupby('gender').size().reset_index(name='count'), 
                x='gender', y='count', 
                title="Number of Credit Card Frauds by Gender")
    st.plotly_chart(fig2)

    # Number of Credit Card Frauds by Job
    
    job_counts = df[df['is_fraud_cat'] == "T"]["job"].value_counts(sort=True, ascending=False).head(10)
    fig3 = px.bar(x=job_counts.index, y=job_counts.values, 
                title="Number of Credit Card Frauds by Job", labels={'x':'Job', 'y':'Count'})
    st.plotly_chart(fig3)


    # Scatter plot using Plotly
    fig = px.scatter(df, x='merch_long', y='merch_lat', color='is_fraud',
                     color_continuous_scale='viridis', opacity=0.5,
                     title='Geospatial Distribution of Transactions (Fraud vs. Non-Fraud)',
                     labels={'merch_long': 'Merchant Longitude', 'merch_lat': 'Merchant Latitude'},
                     hover_data={'is_fraud': True},
                     range_color=[0, 1])
    fig.update_coloraxes(colorbar_title='0: Non-Fraud, 1: Fraud')
    
    # Display the plot in Streamlit
    st.plotly_chart(fig)
    fig = px.scatter(df, x='long', y='lat', color='is_fraud',
                     color_continuous_scale='viridis', opacity=0.5,
                     title='Geospatial Distribution of Transactions (Fraud vs. Non-Fraud)',
                     labels={'long': 'Longitude', 'lat': 'Latitude'},
                     hover_data={'is_fraud': True},
                     range_color=[0, 1])
    fig.update_coloraxes(colorbar_title='0: Non-Fraud, 1: Fraud')
    
    # Display the plot in Streamlit
    st.plotly_chart(fig)
    categorical_columns = ['merchant','city_pop']

    for column in categorical_columns:
        st.subheader(f"Distribution of {column}")
        fig = px.bar(x=df[column].value_counts().index, y=df[column].value_counts().values, 
                    title=f'Distribution of {column}')
        fig.update_xaxes(title_text='Category')
        fig.update_yaxes(title_text='Count')
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)
    

if __name__ == "__main__":
    app()





