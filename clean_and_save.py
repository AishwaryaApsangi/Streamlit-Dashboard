import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = [word for word in text.split() if word not in stop_words]
    return ' '.join(tokens)

def load_and_clean(filepath="C:/Users/aishwarya/OneDrive - Bentley University/Desktop/CS - 370/amazon_reviews_us_Electronics_v1_00.tsv"):
    df = pd.read_csv(filepath, sep='\t', on_bad_lines='skip')
    df = df[['product_id', 'product_title', 'star_rating', 'review_body']].dropna()
    df['clean_review'] = df['review_body'].astype(str).apply(clean_text)
    df['review_length'] = df['clean_review'].apply(lambda x: len(x.split()))
    df = df[df['review_length'] > 5]

    analyzer = SentimentIntensityAnalyzer()
    def get_sentiment(text):
        score = analyzer.polarity_scores(text)['compound']
        return 'Positive' if score >= 0.05 else 'Negative' if score <= -0.05 else 'Neutral'

    df['sentiment'] = df['clean_review'].apply(get_sentiment)
    df = df.sample(n=20000, random_state=42).reset_index(drop=True)
    df.to_csv("pythonProjectCS370/amazon_reviews_cleaned_sampled.csv", index=False)
    print("✅ Cleaned data saved to 'dashboard/amazon_reviews_cleaned_sampled.csv'")

if __name__ == "__main__":
    load_and_clean()
