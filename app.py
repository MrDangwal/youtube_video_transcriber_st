import streamlit as st
from faster_whisper import WhisperModel
import pandas as pd
import os
import time
from fake_useragent import UserAgent
import requests
from pytube import YouTube


def download_youtube_video(url):
    global filename
    st.write("Downloading YouTube video...")

    progress_bar = st.progress(0)
    for percent_complete in range(0, 101, 10):
        time.sleep(0.1)
        progress_bar.progress(percent_complete)

    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers, stream=True)
    video = YouTube(url)
    filename = f"{video.title}.mp3"

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return filename

def transcribe_audio(filename):
    st.write("Transcribing audio...")

    
    progress_bar = st.progress(0)
    for percent_complete in range(0, 101, 10):
        time.sleep(0.1)
        progress_bar.progress(percent_complete)

    model = WhisperModel("tiny.en")
    segments, info = model.transcribe(filename)
    return segments

def save_transcription(segments, output_filename):
    st.write("Processing transcription...")

    
    progress_bar = st.progress(0)
    for percent_complete in range(0, 101, 10):
        time.sleep(0.1)
        progress_bar.progress(percent_complete)

    start_times = []
    end_times = []
    texts = []
    for segment in segments:
        start_times.append(segment.start)
        end_times.append(segment.end)
        texts.append(segment.text)

    df = pd.DataFrame({'Start Time': start_times, 'End Time': end_times, 'Text': texts})

    st.write("Saving transcription data...")

    
    progress_bar = st.progress(0)
    for percent_complete in range(0, 101, 10):
        time.sleep(0.1)
        progress_bar.progress(percent_complete)

    df.to_csv(output_filename, index=False)
    os.remove(filename)
    st.write("Transcription data saved successfully!")

def main():
    st.title("YouTube Audio Transcription")

    global filename  
    youtube_url = st.text_input("Enter YouTube URL:")
    output_filename = st.text_input("Enter output filename:", "transcription_data.csv")

    if st.button("Download and Transcribe"):
        
        filename = download_youtube_video(youtube_url)

        
        segments = transcribe_audio(filename)

        
        save_transcription(segments, output_filename)

        st.success("Transcription completed!")

        
        st.write("Preview Transcription:")
        df = pd.read_csv(output_filename)
        st.write(df.head(10))  

        
        st.download_button(
            label="Download Transcription Data",
            data=df.to_csv(index=False).encode(),
            file_name=output_filename,
            key="download_button"
        )

if __name__ == "__main__":
    main()
