
# 🔮 Bhāva Prediction Tool by Mahān

A semantic NLP-powered tool to predict **Bhāvas** (emotional essences) from user input and suggest related Bhāvas based on meaning similarity.

This tool bridges classical **Sanskrit Bhāva–Chakra–Rasa** wisdom with modern AI. Built using **Streamlit**, it features emoji-enhanced Bhāva cards, CSV exports, and radial trend visualizations.

---

## 🌟 Features

- 🧘 Predict dominant **Bhāva** from user input  
- 🔄 Suggest top 5 Bhāvas using semantic similarity  
- 🌀 Chakra + 🎭 Rasa + 🕉 Sanskrit Meaning integration  
- 🧾 Bhāva history with autosave  
- 📤 CSV export of logs  
- 🪷 Bhāva Wheel (radial bar chart)  

---

## 🧠 Master Bhāva Map

Each Bhāva is mapped to:

- 🌀 **Chakra** (e.g., Ājñā 👁)  
- 🎭 **Rasa** (e.g., Karuṇā 💙)  
- 🕉 **Sanskrit Meaning**

All data is stored in:

```
📁 ./plc_streamlit_tool/assets/bhava_chakra_rasa_map.json
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourname/bhava-prediction-tool.git
cd bhava-prediction-tool
pip install -r requirements.txt
streamlit run plc_streamlit_tool/app.py
```

---

## 📁 Project Structure

```
bhava-prediction-tool/
├── plc_streamlit_tool/
│   ├── app.py                       ← Streamlit app entrypoint
│   ├── bhava_predictor.py          ← Bhāva prediction + similarity engine
│   ├── radial_chart.py             ← Bhāva wheel visualizer
│   └── assets/
│       └── bhava_chakra_rasa_map.json  ← Chakra–Rasa–Bhāva master glossary
├── requirements.txt                ← Python dependencies
└── README.md                       ← This file
```

---

## 🛠 Tech Stack

- 🐍 Python 3.10+
- ⚡ Streamlit
- 🤗 HuggingFace Transformers (optional)
- 📊 Plotly / Matplotlib for visualizations
- 🧠 Custom NLP similarity engine

---

## 📤 Export Options

- ✨ Bhāva logs as CSV
- 📈 Radial Bhāva visual as PNG (optional)
- 🗃️ Future plan: Bhāva JSON export for API use

---

## 📜 Credits

Crafted with devotion by **Mahān**.  
Inspired by Nāṭyaśāstra, Yoga philosophy, and AI-driven Sanskritic exploration.

---

## 📫 Contribute

Want to add more Bhāvas, Rasas, or Chakra mappings?  
Fork this repo and submit a pull request or raise an issue 🙌

---

## 🕉 License

MIT License © Mahān Ravindra  
Use freely. Attribute wisely. Expand consciously.
