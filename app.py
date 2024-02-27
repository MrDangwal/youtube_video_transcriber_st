import streamlit as st
from faster_whisper import WhisperModel
import pandas as pd
import os
import time
import youtube_dl
from fake_useragent import UserAgent
from urllib.parse import urlparse, parse_qs

def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get('v')
    if video_id:
        return video_id[0]
    else:
        return None

def download_youtube_video(url):
    global filename
    st.write("Downloading YouTube video...")

    progress_bar = st.progress(0)
    for percent_complete in range(0, 101, 10):
        time.sleep(0.1)
        progress_bar.progress(percent_complete)

    video_id = extract_video_id(url)
    if not video_id:
        st.error("Invalid YouTube URL. Please provide a valid YouTube video URL.")
        return None

    yt = YoutubeDL()
    info_dict = yt.extract_info(video_id, download=True)
    filename = f"{info_dict['title']}.mp3"
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
