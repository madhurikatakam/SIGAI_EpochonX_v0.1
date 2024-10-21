# Audio Summarizer with Google Generative AI

## Project Objectives

The Audio Summarizer project aims to provide a user-friendly web application that allows users to upload audio files and receive a concise summary of the spoken content. This application utilizes Google Generative AI for summarization, transcription capabilities to convert audio to text, and language detection to identify the language of the transcript. The primary objectives are:

- Enable users to upload audio files in various formats (MP3, WAV, M4A).
- Transcribe the uploaded audio files into text.
- Detect the language of the transcribed text.
- Generate a summary of the transcribed content using Google Generative AI.
- Allow users to download the generated summary as a text file.

## Setup Instructions

To set up and run the Audio Summarizer project locally, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/audio-summarizer.git
   cd audio-summarizer

2. **Create virtual environment**
   ``` python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**
   - Create a .env file in the root directory of the project to store your Google API key.
     GOOGLE_API_KEY=your_google_api_key

   - Then install the necessary Python packages:
    pip install -r requirements.txt

4. **Run the Application:**
   streamlit run app.py



