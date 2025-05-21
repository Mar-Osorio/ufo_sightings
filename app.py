import streamlit as st
import pandas as pd
import plotly.express as px
import datetime


df = pd.read_csv("ufo_sightings_scrubbed.csv")  
df.columns = df.columns.str.strip().str.lower() 
df = df.dropna()
df["datetime"] = pd.to_datetime(df["datetime"])
df["duration (seconds)"] = pd.to_numeric(df["duration (seconds)"], errors='coerce')


st.title("🛸 Unidentified Aerial Phenomena Sightings")

st.subheader("Welcome, earthlings👽")

#Boton histograma shape 
if st.button("Show Sightings by Shape"):
    fig = px.histogram(df, x="shape", color_discrete_sequence=["MediumPurple"])  
    st.plotly_chart(fig)

#Boton histograma country 
if st.button("Show Sightings by Country"):
    fig = px.histogram(df, x="country", color_discrete_sequence=["MediumPurple"]) 
    st.plotly_chart(fig) 

#Boton histograma state 
if st.button("Show Sightings by State"):
    fig = px.histogram(df, x="state", color_discrete_sequence=["MediumPurple"]) 
    st.plotly_chart(fig) 

#Boton scatter
if st.button("Show Duration vs Date"):
    fig = px.scatter(df, x="datetime", y="duration (seconds)", color_discrete_sequence=["MediumPurple"])
    st.plotly_chart(fig)


#mapa
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
map_df = df[["latitude", "longitude"]]
st.header("UAP Sightings Map")
st.map(map_df)

#read about it 
selected_date = st.date_input("Pick a date to see sightings", value=datetime.date(2023, 1, 1))

filtered_by_date = df[df["datetime"].dt.date == selected_date]

if not filtered_by_date.empty:
    st.write(f"👀 Sightings on {selected_date}:")
    for i, row in filtered_by_date.iterrows():
        st.write(f"- {row['datetime'].strftime('%H:%M')} — {row.get('comments', 'No comment available')}")
else:
    st.write(f"No sightings found on {selected_date}.")

map_df = filtered_by_date[["latitude", "longitude"]]
st.map(map_df)


#report
user_comment = st.text_input("👽 Report your own sighting!")

if user_comment:
    st.write("📝 You said:", user_comment)


