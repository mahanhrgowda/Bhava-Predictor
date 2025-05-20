from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

MASTER_BHAVAS = [
    "Śāntiḥ", "Ānandaḥ", "Bhaktiḥ", "Jñānam", "Karunā", "Āstikyam", "Vīryam", "Utsāhaḥ",
    "Rāgaḥ", "Dainyaḥ", "Harṣaḥ", "Īrṣyā", "Krodhaḥ", "Bhayam", "Vairāgyam", "Mādhuryam",
    "Dhṛtiḥ", "Nirvedaḥ", "Ākrośaḥ", "Āścaryaṁ", "Mohaḥ", "Lajjā"
]

SAMPLE_INTENTS = {
    bhava: [
        f"This expresses the quality of {bhava}",
        f"A feeling related to {bhava}",
        f"Embodies the trait of {bhava}"
    ] for bhava in MASTER_BHAVAS
}

def get_training_data():
    X, y = [], []
    for bhava, phrases in SAMPLE_INTENTS.items():
        for phrase in phrases:
            X.append(phrase)
            y.append(bhava)
    return X, y

def train_intent_model():
    X, y = get_training_data()
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=2000))
    ])
    return pipeline.fit(X, y)

def predict_intent(model, sentence):
    return model.predict([sentence])[0]