import reflex as rx
from reactpy import component, html

@component
def AudioRecorder():
    return html.div(
        html.button("Start Recording", id="start-recording"),
        html.button("Stop Recording", id="stop-recording"),
        html.audio(id="audio-playback", controls=True),
    )

def index():
    return rx.vstack(
        rx.heading("Audio Recorder"),
        AudioRecorder(),
    )