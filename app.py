import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

st.title('Shampoo Sales App')
st.text('This is a web app to allow users to forecast sales of Shampoo')

df=pd.read_csv('data.csv')
df['Month']=pd.to_datetime(df['Month'],format='%Y-%m')
df.set_index('Month',inplace=True)

st.header('Dataset')
st.dataframe(df.head().T)

st.header('Shampoo Sales')
df.plot(figsize=(12,4))
plt.ylabel('Sales')
plt.title("Shampoo Sales over Time")
plt.xlabel('Time')
st.pyplot(plt)

model = sm.load('model.pkl')

st.header('Input Slider')
step = st.slider("Select months to forecast:",0,48)

st.header('Output Forecast')
if step!=0:
    predicted_SARIMA = model.forecast(steps=step)
    predicted_SARIMA = pd.DataFrame(predicted_SARIMA)
    predicted_SARIMA.rename(columns = {'predicted_mean':'Sales'}, inplace = True)
    df = pd.concat([df,predicted_SARIMA], axis=0)

    df.plot(figsize=(12,4))
    plt.ylabel('Sales')
    plt.title("Predicted")
    plt.xlabel('Time')
    plt.axvline(x='2003-12-01',linewidth=2,color='orange',alpha=0.75,label='forecast after this point',linestyle='dashed')
    plt.legend(loc=0)
    st.pyplot(plt)

