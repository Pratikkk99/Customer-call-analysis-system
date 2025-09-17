# Customer-call-analysis-system

# 📞 Customer Call Analysis System

A lightweight, AI-powered Streamlit app that analyzes customer call transcripts using Google's Gemini API. It generates concise summaries and detects sentiment to help businesses quickly understand and act on customer conversations.

---

## 🚀 Features

- ✨ Summarizes customer calls in 2–3 sentences using Gemini
- 😊 Detects sentiment: Positive, Neutral, or Negative
- 📄 Saves results to a CSV file for historical tracking
- 🧠 Built with Streamlit for rapid prototyping and clean UI

---

## 🧱 Tech Stack

| Layer        | Tools Used                          |
|--------------|-------------------------------------|
| Frontend     | Streamlit                           |
| Backend      | Python, Google Generative AI SDK    |
| Data Storage | Pandas, CSV                         |
| Environment  | dotenv, OS                          |

---

## 🧑‍💻 How It Works

1. **User Input**: Paste a customer call transcript into the Streamlit text area.
2. **Gemini Integration**:
   - Generates a summary of the call.
   - Classifies sentiment as Positive, Neutral, or Negative.
3. **Display & Save**:
   - Shows results on the UI.
   - Appends the data to `call_analysis.csv`.
4. **Error Handling**: Gracefully handles missing input or API errors.

