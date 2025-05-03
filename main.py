# ================================================
# Streamlit Final Dashboard (Goodreads Layout Style)
# ================================================

import streamlit as st
import pandas as pd
import numpy as np
import nltk
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.add_vertical_space import add_vertical_space

# Download stopwords once if not present
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    # Page Config
    st.set_page_config(page_title="Amazon Reviews Explorer", layout="wide")

    # Load animation
    lottie_amazon = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dyfjzxcj.json")
    if lottie_amazon:
        st_lottie(lottie_amazon, speed=1, height=200, key="header")

    # Load local cleaned CSV file (ensure it's in the same folder)
    df = pd.read_csv("amazon_reviews_cleaned.csv")

    # Dashboard Title
    row0_spacer1, row0_1, row0_spacer2 = st.columns((0.1, 3.2, 0.1))
    with row0_1:
        st.title("🔎 Amazon Electronics Reviews Explorer")
    add_vertical_space()

    st.markdown("Analyze Amazon Electronics reviews by sentiment, topic modeling, and star ratings. 📦✨")

    # Dataset Overview
    st.header("Dataset Overview")
    st.dataframe(df[['product_id', 'product_title', 'star_rating', 'sentiment', 'clean_review']].head())

    # Sentiment Distribution
    st.header("Sentiment Analysis")
    sentiment_counts = df['sentiment'].value_counts(normalize=True)
    fig_sentiment = px.bar(
        sentiment_counts,
        x=sentiment_counts.index,
        y=sentiment_counts.values,
        labels={'x': 'Sentiment', 'y': 'Percentage'},
        title="Sentiment Distribution",
        color_discrete_sequence=["#9EE6CF"]
    )
    st.plotly_chart(fig_sentiment, use_container_width=True)

    # Star Rating Distribution
    st.header("Star Rating Distribution")
    fig_stars = px.histogram(
        df,
        x="star_rating",
        nbins=5,
        title="Distribution of Star Ratings",
        color_discrete_sequence=["#9EE6CF"]
    )
    st.plotly_chart(fig_stars, use_container_width=True)

    # Word Cloud
    st.header("Common Words in Reviews")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['clean_review']))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)

    # Footer
    st.markdown("***")
    st.markdown("Made by Ash Apsangi | Amazon Electronics Reviews Explorer 2025")

if __name__ == "__main__":
    main()

