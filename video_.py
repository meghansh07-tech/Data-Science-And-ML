import streamlit as st

st.title("App Demo Video")

# Load and play your screen recording
video_file = open("screen_record.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)