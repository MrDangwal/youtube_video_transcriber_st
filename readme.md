# YouTube Video Transcriber

This is a simple web application built using Streamlit that allows users to transcribe audio from YouTube videos. The application utilizes the `faster_whisper` library for transcription and `pytube` for downloading YouTube videos.

## Demo

You can try the application live on [YouTube Video Transcriber](https://youtube-video-transcriber.streamlit.app/).

## Usage

1. Enter the YouTube URL of the video you want to transcribe.
2. Specify the desired output filename for the transcription data (default is `transcription_data.csv`).
3. Click the "Download and Transcribe" button.

The application will download the audio from the provided YouTube URL, transcribe it, and save the transcription data to a CSV file. A preview of the transcription data will be displayed, and you can download the full transcription data as a CSV file.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

4. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to use the application.

## Dependencies

- Streamlit
- faster_whisper
- pytube
- pandas


---
