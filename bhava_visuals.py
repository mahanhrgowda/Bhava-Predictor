BHAVA_VISUALS = {
    "Śāntiḥ": {"emoji": "🕊️", "color": "#A0E7E5"},
    "Ānandaḥ": {"emoji": "💗", "color": "#FFDEE9"},
    "Bhaktiḥ": {"emoji": "🙏", "color": "#D1B3FF"},
    "Jñānam": {"emoji": "📘", "color": "#89CFF0"},
    "Karunā": {"emoji": "💙", "color": "#FFB6C1"},
    "Āstikyam": {"emoji": "🕊️", "color": "#CCE5FF"},
    "Vīryam": {"emoji": "⚔️", "color": "#FF7F50"},
    "Utsāhaḥ": {"emoji": "🔥", "color": "#FFA500"},
    "Rāgaḥ": {"emoji": "💘", "color": "#FF69B4"},
    "Dainyaḥ": {"emoji": "😢", "color": "#AEC6CF"},
    "Harṣaḥ": {"emoji": "😂", "color": "#FFFF66"},
    "Īrṣyā": {"emoji": "😠", "color": "#FF9999"},
    "Krodhaḥ": {"emoji": "🔥", "color": "#DC143C"},
    "Bhayam": {"emoji": "😱", "color": "#FF6666"},
    "Vairāgyam": {"emoji": "🕊️", "color": "#E0FFFF"},
    "Mādhuryam": {"emoji": "💞", "color": "#FFC0CB"},
    "Dhṛtiḥ": {"emoji": "⚔️", "color": "#FF4500"},
    "Nirvedaḥ": {"emoji": "😌", "color": "#E6E6FA"},
    "Ākrośaḥ": {"emoji": "🔥", "color": "#8B0000"},
    "Āścaryaṁ": {"emoji": "🌠", "color": "#D8BFD8"},
    "Mohaḥ": {"emoji": "😵", "color": "#F08080"},
    "Lajjā": {"emoji": "🙈", "color": "#E0B0FF"}
}

def get_bhava_visual(bhava):
    return BHAVA_VISUALS.get(bhava, {"emoji": "❓", "color": "#CCCCCC"})