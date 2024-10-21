import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from groq import Groq
from langdetect import detect

# Load environment variables from .env file
load_dotenv()
client = Groq(api_key='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')

# Configure Google Generative AI with your API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Define the summarization function
def summarize_text(text):
    # Define the model and prompt for summarization
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Summarize the following text:\n\n{text}"

    # Generate the summary using the API
    response = model.generate_content(prompt)
    summary = response.text
    
    return summary

# Define function to handle audio transcription
def transcribe_audio(audio_file):
    if not os.path.exists(audio_file):
        return None, "Audio file not found."

    with open(audio_file, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_file, file.read()),
            model="whisper-large-v3",
            language="en",
            response_format="verbose_json",
        )
    return transcription.text

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"
    
# Streamlit UI
st.title("Audio Summarizer")

# Upload audio file
uploaded_audio = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

# Initialize summary variable
summary = ""

# Display a summarize button
if st.button("Summarize"):
    if uploaded_audio is not None:
        # Save the audio file to a temporary path
        audio_path = os.path.join("", uploaded_audio.name)
        with open(audio_path, "wb") as f:
            f.write(uploaded_audio.getbuffer())
            
        # Transcribe the audio
        transcript = transcribe_audio(audio_path)

        if transcript:
            detected_language = detect_language(transcript)
            st.write(f"Detected Language: {detected_language}")

            # Show the transcript (optional)
            # st.write("Transcript of the audio:")
            # st.write(transcript)

            # Summarize the transcript
            summary = summarize_text(transcript)

            # Show the summary
            st.write("Summary of the transcript:")
            st.write(summary)
        else:
            st.error("Failed to transcribe audio.")

    else:
        st.warning("Please upload an audio file before summarizing.")

# Create a download button
if summary:
    summary_file = "summary.txt"
    with open(summary_file, "w") as f:
        f.write(summary)

    st.download_button(
        label="Download Summary",
        data=open(summary_file, "rb"),
        file_name=summary_file,
        mime="text/plain"
    )
