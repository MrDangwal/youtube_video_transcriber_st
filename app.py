import streamlit as st
from faster_whisper import WhisperModel
from pytube import YouTube
import pandas as pd
import os
import time

# Define filename as a global variable
filename = ""

def download_youtube_video(url):
    global filename  # Use the global variable
    st.write("Downloading YouTube video...")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    filename = f"{yt.title}.mp3"
    video.download(output_path=".", filename=filename)
    return filename

def transcribe_audio(filename):
    st.write("Transcribing audio...")
    model = WhisperModel("tiny.en")
    segments, info = model.transcribe(filename)

    # Simulate progress with a dummy progress bar
    for i in range(100):
        time.sleep(0.05)  # Simulate processing time
        st.progress(i + 1)

    return segments

def save_transcription(segments, output_filename):
    st.write("Processing transcription...")
    start_times = []
    end_times = []
    texts = []
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

    global filename  # Use the global variable
    youtube_url = st.text_input("Enter YouTube URL:")
    output_filename = st.text_input("Enter output filename:", "transcription_data.csv")

    if st.button("Download and Transcribe"):
        # Download YouTube video
        filename = download_youtube_video(youtube_url)

        # Transcribe audio
        segments = transcribe_audio(filename)

        # Save transcription
        save_transcription(segments, output_filename)

        st.success("Transcription completed!")

        # Show preview of the transcription
        st.write("Preview Transcription:")
        df = pd.read_csv(output_filename)
        st.write(df.head(10))  # Show first 10 rows as a preview

        # Provide download button
        st.download_button(
            label="Download Transcription Data",
            data=df.to_csv(index=False).encode(),
            file_name=output_filename,
            key="download_button"
        )

if __name__ == "__main__":
    main()
