import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.title("Netflix Data Analysis Dashboard")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")

type_count = df['type'].value_counts()

fig1, ax1 = plt.subplots()
sns.barplot(x=type_count.index, y=type_count.values, ax=ax1)

ax1.set_title("Movies vs TV Shows on Netflix")
ax1.set_xlabel("Type")
ax1.set_ylabel("Count")

st.pyplot(fig1)

# Top 10 Countries
st.subheader("Top Countries Producing Content")

country = df['country'].value_counts().head(10)

fig2, ax2 = plt.subplots()
country.plot(kind='bar', ax=ax2)
ax2.set_title("Top 10 Countries on Netflix")

st.pyplot(fig2)

# Release year trend
st.subheader("Content Released Over Years")

year_data = df['release_year'].value_counts().sort_index()

fig3, ax3 = plt.subplots()
year_data.plot(ax=ax3)

ax3.set_title("Netflix Content Growth")

st.pyplot(fig3)

# Genre analysis
st.subheader("Top Genres")

genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

fig4, ax4 = plt.subplots()
top_genres.plot(kind='bar', ax=ax4)

ax4.set_title("Top Genres on Netflix")

st.pyplot(fig4)

# Content Ratings
st.subheader("Content Rating Distribution")

rating = df['rating'].value_counts().head(10)

fig4, ax4 = plt.subplots()
rating.plot(kind='bar', ax=ax4)

ax4.set_title("Top Content Ratings on Netflix")

st.pyplot(fig4)

# Pie Chart
st.subheader("Movies vs TV Shows Percentage")

fig5, ax5 = plt.subplots()

df['type'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax5
)

ax5.set_ylabel("")

st.pyplot(fig5)

# Top Genres
st.subheader("Top Genres on Netflix")

genres = df['listed_in'].str.split(', ', expand=True).stack()

top_genres = genres.value_counts().head(10)

fig6, ax6 = plt.subplots()
top_genres.plot(kind='bar', ax=ax6)

ax6.set_title("Top Genres on Netflix")

st.pyplot(fig6)