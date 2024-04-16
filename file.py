import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

colors = [
    "#5CA8D9",  # Azul claro
    "#36B2E0",
    "#67C5EB",
    "#8FD9F4",
    "#B2E7FA",
    "#D5F5FF",  # Azul cielo
    "#8DEBC4",  # Verde menta
    "#60E1A7",
    "#33D78B",
    "#06CD6F"   # Esmeralda
]

st.title("Feminism")

df=pd.read_csv("data.csv")

st.write("Are feminist movies good?")
st.write("We have merged the IMDB data from movies with the bechdel test data from Kaggle and decided to investigate the various relationships between art and sociology.")
st.write("The data we have used is the following:")


st.write(df)

st.markdown("---")
st.write("")
st.subheader("Category - Feminism realtionship")

st.write("We have decided to investigate the relationship between the category of the movie and the feminist score.")
#primer grafico

group=df.groupby(["feminism","titleType"],as_index=False).mean(numeric_only=True)
fig = px.bar(group, x="feminism", y="stars", color="titleType",barmode="group",color_discrete_sequence=colors)
fig.update_layout(
  paper_bgcolor = "rgba(0,0,0,0)",
)

st.plotly_chart(fig, use_container_width=True)

#segundo grafico
genre2 = st.radio(
    "Select the segmentation...",
    ["first_genre", "second_genre","third_genre"],
    #captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."]
    )

option = st.selectbox(
    'How would you like to be contacted?',
    ('stars', 'year', 'runtimeMinutes'))

group=df.groupby(["titleType",genre2],as_index=False).mean(numeric_only=True)
fig = px.scatter(group, x="feminism", y=option,color="titleType",hover_name=genre2,marginal_y="violin",
           marginal_x="box", trendline="ols",color_discrete_sequence=colors)   #
fig.update_layout(
  paper_bgcolor = "rgba(0,0,0,0)",

)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Temporary Evolution of Feminism")
st.write("We have decided to investigate the evolution of the feminist score over the years.")

#tercer grafico
genre = st.radio(
    "Select the segmentation",
    ["first_genre", "titleType"],
    #captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."]
    )

tograph=df.groupby(["year",genre],as_index=False).mean(numeric_only=True)


fig=px.area(tograph,x="year",y="feminism",color=genre,color_discrete_sequence=colors)
fig.update_layout(
  paper_bgcolor = "rgba(0,0,0,0)",

)
st.plotly_chart(fig, use_container_width=True)
