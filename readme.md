YouTube Video Transcriber
This is a simple web application built using Streamlit that allows users to transcribe audio from YouTube videos. The application utilizes the faster_whisper library for transcription and pytube for downloading YouTube videos.

Demo
You can try the application live on YouTube Video Transcriber.

Usage
Enter the YouTube URL of the video you want to transcribe.
Specify the desired output filename for the transcription data (default is transcription_data.csv).
Click the "Download and Transcribe" button.
The application will download the audio from the provided YouTube URL, transcribe it, and save the transcription data to a CSV file. A preview of the transcription data will be displayed, and you can download the full transcription data as a CSV file.

Installation
To run the application locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
streamlit run app.py
Open your web browser and go to http://localhost:8501 to use the application.
Dependencies
Streamlit
faster_whisper
pytube
pandas
