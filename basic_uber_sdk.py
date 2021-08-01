from pandas import to_datetime
import streamlit as st
import pandas as pd

@st.cache
def read_data():
    path = "uber_pickup_data/archive/uber-raw-data-jul14.csv"
    print("Starting the uber predict ....")
    df = pd.read_csv(path, encoding='utf-8')
    df.rename(columns={"Lat":"lat", "Lon":"lon", "Date/Time":"Datetime"}, inplace=True)
    return df

if __name__ == '__main__':
    df = read_data()
    df_date= pd.to_datetime(df['Datetime'])
    df.info()

    cust = st.radio( options=df['Base'].unique(), label="Select")
    num = st.slider(label="Select the date range")
    map = st.map(df.head(num))