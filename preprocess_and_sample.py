# preprocess_and_sample.py

import pandas as pd
import re
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))

# Load TSV
df = pd.read_csv(
    "C:/Users/aishwarya/OneDrive - Bentley University/Desktop/CS - 370/amazon_reviews_us_Electronics_v1_00.tsv",
    sep="\t",
    on_bad_lines="skip"
)

# Keep necessary columns
df = df[['product_id', 'product_title', 'star_rating', 'review_body']].dropna()

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = [word for word in text.split() if word not in stop_words]
    return ' '.join(tokens)

df['clean_review'] = df['review_body'].apply(clean_text)
df['review_length'] = df['clean_review'].apply(lambda x: len(x.split()))
df = df[df['review_length'] > 5]

# VADER Sentiment
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['clean_review'].apply(get_sentiment)

# Sample for dashboard
df_sampled = df.sample(n=20000, random_state=42).reset_index(drop=True)

# Save to CSV
df_sampled.to_csv("amazon_reviews_cleaned_sampled.csv", index=False)

print("✅ Saved: amazon_reviews_cleaned_sampled.csv")
