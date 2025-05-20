import streamlit as st
import pandas as pd
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from plc_bhava_intent import train_intent_model, predict_intent
from bhava_visuals import get_bhava_visual

st.set_page_config(page_title="Bhāva Prediction Tool by Mahān", layout="wide")

st.title("🧘‍♂️ Bhāva Prediction Tool by Mahān")
st.markdown("**Enter a sentence to predict its Bhāva and explore deeper connections.**")

@st.cache_resource
def get_intent_model():
    return train_intent_model()

model = get_intent_model()

with open("assets/bhava_chakra_rasa_map.json", encoding="utf-8") as f:
    bhava_data = json.load(f)

bhava_meanings = [entry["meaning"] for entry in bhava_data]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(bhava_meanings)

LOG_PATH = "bhava_history_log.csv"
if os.path.exists(LOG_PATH):
    history = pd.read_csv(LOG_PATH).values.tolist()
else:
    history = []

if "history" not in st.session_state:
    st.session_state.history = history

user_input = st.text_input("✍️ Enter your sentence:", placeholder="e.g. I feel deep compassion for everyone")

if user_input:
    bhava = predict_intent(model, user_input)
    visual = get_bhava_visual(bhava)

    st.markdown(f"<div style='background-color:{visual['color']};padding:2rem;border-radius:10px;text-align:center'>"
                f"<h1>{visual['emoji']} {bhava}</h1></div>", unsafe_allow_html=True)

    entry = (user_input, bhava, visual["emoji"], visual["color"])
    st.session_state.history.append(entry)
    pd.DataFrame(st.session_state.history, columns=["Sentence", "Bhāva", "Emoji", "Color"]).to_csv(LOG_PATH, index=False)

    st.subheader("🔄 Suggested Bhāvas")
    input_vec = vectorizer.transform([user_input])
    sim_scores = cosine_similarity(input_vec, tfidf_matrix).flatten()
    for idx in sim_scores.argsort()[::-1][:5]:
        entry = bhava_data[idx]
        st.markdown(
            f"<div style='background-color:#f9f9f9;padding:0.5rem;border-radius:5px;margin-bottom:0.5rem;'>"
            f"🔸 <b>{entry['bhava']}</b> — <i>{entry['meaning']}</i> "
            f"({entry['chakra']} {entry['chakra_emoji']}, {entry['rasa']} {entry['rasa_emoji']})</div>",
            unsafe_allow_html=True)

if st.session_state.history:
    st.subheader("🧾 Bhāva History")
    for sentence, bhava, emoji, color in reversed(st.session_state.history[-10:]):
        st.markdown(f"<div style='background-color:{color};padding:0.5rem 1rem;border-radius:6px;'>"
                    f"<b>{emoji} {bhava}</b> — <i>{sentence}</i></div>", unsafe_allow_html=True)

    st.subheader("📤 Export History")
    export_data = pd.DataFrame(st.session_state.history, columns=["Sentence", "Bhāva", "Emoji", "Color"])
    st.download_button("Download CSV", export_data.to_csv(index=False), "bhava_history.csv", "text/csv")
