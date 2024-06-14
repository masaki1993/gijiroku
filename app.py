import streamlit as st
import openai
import os

# Set OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

def transcribe_audio(api_key, audio_file_path):
    openai.api_key = api_key

    with open(audio_file_path, "rb") as audio_file:
        response = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return response['text']

def summarize_text(api_key, text):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150
    )
    return response['choices'][0]['text']

st.title("Audio Transcription and Summarization")

audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

if audio_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.getbuffer())

    transcript = transcribe_audio(st.secrets["openai_api_key"], "temp_audio.wav")
    st.write("Transcription Result:")
    st.write(transcript)

    summarized_text = summarize_text(st.secrets["openai_api_key"], transcript)
    st.write("Summarized Text:")
    st.write(summarized_text)