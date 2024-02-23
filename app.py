import streamlit as st
from faster_whisper import WhisperModel
from pytube import YouTube
import pandas as pd
import os

def download_youtube_transcribe(url, output_filename, progress_bar):
    st.write("Downloading YouTube video...")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    filename = f"{yt.title}.mp3"
    video.download(output_path=".", filename=filename)
    
    progress_bar.progress(30)  # Progress: 30%
    st.write("Transcribing audio...")
    model = WhisperModel("tiny.en")
    segments, info = model.transcribe(filename)
    
    start_times = []
    end_times = []
    texts = []

    st.write("Processing transcription...")
    progress_bar.progress(60)  # Progress: 60%
    for segment in segments:
        start_times.append(segment.start)
        end_times.append(segment.end)
        texts.append(segment.text)
    
    df = pd.DataFrame({'Start Time': start_times, 'End Time': end_times, 'Text': texts})

    st.write("Saving transcription data...")
    progress_bar.progress(90)  # Progress: 90%
    df.to_csv(output_filename, index=False)

    os.remove(filename)
    progress_bar.progress(100)  # Progress: 100%
    st.write("Transcription data saved successfully!")

def main():
    st.title("YouTube Audio Transcription")

    youtube_url = st.text_input("Enter YouTube URL:")
    output_filename = st.text_input("Enter output filename:", "transcription_data.csv")

    if st.button("Download and Transcribe"):
        progress_bar = st.progress(0)  # Progress: 0%
        download_youtube_transcribe(youtube_url, output_filename, progress_bar)
        st.success("Transcription completed!")

        st.write("Preview Transcription:")
        df = pd.read_csv(output_filename)
        st.write(df.head(10))  # Show first 10 rows as a preview

        if st.button("Download Transcription"):
            with open(output_filename, "rb") as file:
                file_contents = file.read()
            st.download_button(label="Download Transcription File", data=file_contents, file_name=output_filename, mime="text/csv")

if __name__ == "__main__":
    main()
