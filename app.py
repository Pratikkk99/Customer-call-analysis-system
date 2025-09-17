import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables if .env exists
load_dotenv()

#  Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCQIqjZ4Sd2hmC100FPxfIO16XB9CrMhy4")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
MODEL = "gemini-1.5-flash"

st.title(" Customer Call Analysis system")

transcript = st.text_area("Paste customer call transcript:", height=200)

if st.button("Analyze"):
    if not transcript.strip():
        st.warning("⚠️ Please enter a transcript.")
    else:
        try:
            #  Get Summary 
            model = genai.GenerativeModel(MODEL)
            summary_resp = model.generate_content(
                f"Summarize the following customer call in 2–3 sentences:\n\n{transcript}"
            )
            summary = summary_resp.text.strip()

            # Get Sentiment
            sentiment_resp = model.generate_content(
                f"Extract the customer's sentiment as Positive, Neutral, or Negative. "
                f"Transcript:\n\n{transcript}"
            )
            sentiment = sentiment_resp.text.strip()

            #  Display results
            st.subheader("Results")
            st.write("**Transcript:**", transcript)
            st.write("**Summary:**", summary)
            st.write("**Sentiment:**", sentiment)

            #  Save to CSV 
            df = pd.DataFrame([[transcript, summary, sentiment]],
                              columns=["Transcript", "Summary", "Sentiment"])
            csv_file = "call_analysis.csv"
            if os.path.exists(csv_file):
                old = pd.read_csv(csv_file)
                df = pd.concat([old, df], ignore_index=True)
            df.to_csv(csv_file, index=False)
            st.success(f"✅ Saved results to {csv_file}")
            st.dataframe(df)

        except Exception as e:
            st.error(f" Error: {e}")
