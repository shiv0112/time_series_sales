import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

st.title('Shampoo Sales App')
st.text('This is a web app to allow users to forecast sales of Shampoo')

df=pd.read_csv('data.csv')
df['Month']=pd.to_datetime(df['Month'])
df.set_index('Month',inplace=True)

st.header('Dataset')
st.dataframe(df.head(7).T)

st.header('Shampoo Sales')
df.plot(figsize=(12,4))
plt.ylabel('Sales')
plt.title("Shampoo Sales over Time")
plt.xlabel('Time')
st.pyplot(plt)

model = sm.load('model.pkl')

st.header('Input Slider')
step = st.slider("Select months to forecast:",1,48,value=0)
st.write(step)
st.write(step+1)

st.header('Output Forecast')
if step!=0:
    predicted_SARIMA = model.forecast(steps=step)
    st.write(predicted_SARIMA)
    plt.plot(df,label='Actual data')
    plt.plot(predicted_SARIMA,label='Predicted Data - SARIMAX')
    plt.grid()
    plt.title('Sarima(2,1,3)x(4,1,1,12): Future Prediction')
    plt.grid()
    st.pyplot(plt)


