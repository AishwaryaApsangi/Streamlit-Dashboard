import streamlit as st
from PIL import Image

st.set_page_config(page_title="Amazon Electronics Dashboard", layout="wide")

st.title("🔎 Amazon Electronics Reviews – Final Project Dashboard")
st.markdown("This dashboard showcases key insights from Amazon Electronics reviews using pre-generated visualizations and a fast-loading layout. ⚡")

st.header("📊 Visual Insights (Static Grid)")

# Image titles and their corresponding filenames (must match filenames in repo!)
images = {
    "Star Rating Distribution": "download.png",
    "Top 10 Most Reviewed Products": "download (2).png",
    "Word Cloud of Frequent Review Terms": "download (1).png",
    "Hierarchical Clustering": "newplot (4).png",
    "Similarity Matrix": "newplot (3).png",
    "Intertopic Distance Map": "newplot (5).png",
    "Topic Word Scores": "newplot (2).png"
}

# Grid layout for image display
rows = [
    ["Star Rating Distribution", "Top 10 Most Reviewed Products"],
    ["Word Cloud of Frequent Review Terms", "Hierarchical Clustering"],
    ["Similarity Matrix", "Intertopic Distance Map"],
    ["Topic Word Scores"]
]

# Display images in layout
for row in rows:
    cols = st.columns(len(row))
    for col, title in zip(cols, row):
        file_path = images[title]
        try:
            image = Image.open(file_path)
            col.image(image, caption=title, use_container_width=True)
        except Exception as e:
            col.error(f"⚠️ Error loading: {title}")
