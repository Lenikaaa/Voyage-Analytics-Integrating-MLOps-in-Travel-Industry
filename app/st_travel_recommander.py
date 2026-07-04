import streamlit as st
import sys
import os
from pathlib import Path

# Add src folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from recommander.preprocessor import build_user_hotel_matrix
from recommander.similarity import compute_user_similarity
from recommander.recommander import recommend_hotels

# ==========================
# Streamlit Page Config
# ==========================
st.set_page_config(
    page_title="Hotel Recommendation System",
    layout="wide"
)

st.title("🏨 Travel Hotel Recommendation System")

# ==========================
# Dataset Path
# ==========================
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = (
    BASE_DIR
    / "data"
    / "hotel_recommander"
    / "hotels.csv"
)

# ==========================
# Build Recommendation Engine
# ==========================
user_hotel_matrix = build_user_hotel_matrix(DATA_PATH)
similarity_df = compute_user_similarity(user_hotel_matrix)

# ==========================
# User Selection
# ==========================
user_id = st.sidebar.selectbox(
    "Select User ID",
    user_hotel_matrix.index.tolist()
)

st.subheader("Recommended Hotels")

# ==========================
# Generate Recommendations
# ==========================
recommendations = recommend_hotels(
    user_id,
    user_hotel_matrix,
    similarity_df
)

# ==========================
# Display Recommendations
# ==========================
if not recommendations:
    st.warning("No recommendations available.")
else:
    for hotel, score in recommendations:
        st.write(
            f"**{hotel}** — Similarity Score: `{round(score, 3)}`"
        )