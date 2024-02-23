import streamlit as st
from faster_whisper import WhisperModel
from pytube import YouTube
import pandas as pd
import os

def download_youtube_transcribe(url, output_filename):
    st.write("Downloading YouTube video...")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    filename = f"{yt.title}.mp3"
    video.download(output_path=".", filename=filename)

    st.write("Transcribing audio...")
    model = WhisperModel("tiny.en")
    segments, info = model.transcribe(filename)

    start_times = []
    end_times = []
    texts = []

    st.write("Processing transcription...")
    for segment in segments:
        start_times.append(segment.start)
        end_times.append(segment.end)
        texts.append(segment.text)

    df = pd.DataFrame({'Start Time': start_times, 'End Time': end_times, 'Text': texts})

    st.write("Saving transcription data...")
    df.to_csv(output_filename, index=False)

    os.remove(filename)
    st.write("Transcription data saved successfully!")

def main():
    st.title("YouTube Audio Transcription")

    youtube_url = st.text_input("Enter YouTube URL:")
    output_filename = st.text_input("Enter output filename:", "transcription_data.csv")

    if st.button("Download and Transcribe"):
        download_youtube_transcribe(youtube_url, output_filename)
        st.success("Transcription completed!")

        st.write("Preview Transcription:")
        df = pd.read_csv(output_filename)
        st.write(df.head(10))  # Show first 10 rows as a preview

if __name__ == "__main__":
    main()
