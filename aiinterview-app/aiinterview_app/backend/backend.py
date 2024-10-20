import reflex as rx
from typing import Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta
from PIL import Image
import time
from pathlib import Path
from urllib.request import urlopen
from PIL import Image
import reflex_webcam as webcam
# from vapi_python import Vapi
# class User(rx.Base):
#     job_description: str
#     resume: str
#     company: str

# Your VAPI assistant credentials
API_KEY = "2b69f505-2aac-410c-bd38-6b8da2baddf8"
ASSISTANT_ID = "4d742d2d-2afe-484b-8eab-4fd5fa41e825"
# vapi = Vapi(api_key=API_KEY)

# Identifies a particular webcam component in the DOM
WEBCAM_REF = "webcam"
VIDEO_FILE_NAME = "video.webm"

# The path containing the app
APP_PATH = Path(__file__)
APP_MODULE_DIR = APP_PATH.parent
SOURCE_CODE = [
    APP_MODULE_DIR.parent.parent / "components/webcam.py",
    APP_PATH,
    APP_MODULE_DIR.parent / "requirements.txt",
]

# Mark Upload as used so StaticFiles can get mounted on /_upload
rx.upload()

class Score(rx.Base):
    value = 1
    box_color = "red"

    def set_value(self, new_value: str):
        self.value = int(new_value)
        self.update_color()

    def update_color(self):
        if self.value < 4:
            self.box_color = "red"
        elif self.value < 8:
            self.box_color = "orange"
        else:
            self.box_color = "green"
    
class State(rx.State):
    last_screenshot: Image.Image | None = None
    last_screenshot_timestamp: str = ""
    loading: bool = False
    recording: bool = False
    """The app state."""
    job_description: str
    resume: str
    company: str
    
    structure: Score = Score()
    relevance: Score = Score()
    volume: Score = Score()
    clarity: Score = Score()
    summary = "You demonstrated strong product management fundamentals, especially in prioritizing features and aligning product goals with business objectives. Your communication about working with cross-functional teams was clear, and you gave solid examples of driving feature development from concept to launch. However, your answers regarding handling unexpected product failures could have been more detailed, and expanding on how you measure product success beyond basic metrics would strengthen your responses."
    recommendation= "You could enhance your approach by discussing risk management and how you handle post-launch issues in more depth. Providing more detailed examples of how you adapt strategy based on stakeholder feedback would also be beneficial. Additionally, sharing insights into customer feedback loops and iterative development processes would showcase a more user-centered product approach."
    next_step = "You show great potential, but a follow-up interview focused on your experience with data-driven decision-making and product iterations based on user feedback would provide further insight. It might also be helpful to complete a product scenario exercise to assess your problem-solving and prioritization skills in a more practical setting before moving forward."       

    def update__info(self, new_jd: str, new_resume: str, new_company: str):
        self.job_description = new_jd
        self.resume = new_resume
        self.company = new_company
    
    def update_score(self, structure :str, relevance :str, volume: str, clarity: str):
        self.structure.set_value(structure)
        self.relevance.set_value(relevance),
        self.volume.set_value(volume),
        self.clarity.set_value(clarity)
    
    def update_report(self, summary: str, recommendation :str, next_step: str):
        self.summary = summary
        self.recommendation = recommendation
        self.next_step = next_step

    def test_increament(self):
        self.structure.set_value("6")
        self.relevance.set_value("3"),
        self.volume.set_value("8"),
        self.clarity.set_value("5")

    def handle_screenshot(self, img_data_uri: str):
        """Webcam screenshot upload handler.
        Args:
            img_data_uri: The data uri of the screenshot (from upload_screenshot).
        """
        if self.loading:
            return
        self.last_screenshot_timestamp = time.strftime("%H:%M:%S")
        with urlopen(img_data_uri) as img:
            self.last_screenshot = Image.open(img)
            self.last_screenshot.load()
            # convert to webp during serialization for smaller size
            self.last_screenshot.format = "WEBP"  # type: ignore

    def _video_path(self) -> Path:
        return Path(rx.get_upload_dir()) / VIDEO_FILE_NAME

    @rx.var(cache=True)
    def video_exists(self) -> bool:
        if not self.recording:
            return self._video_path().exists()
        return False

    def on_start_recording(self):
        self.recording = True
        print("Started recording")
        print(self.company)
        # vapi.start(assistant_id=ASSISTANT_ID)
        with self._video_path().open("wb") as f:
            f.write(b"")

    def _strip_codec_part(self, chunk: str) -> str:
        parts = chunk.split(";")
        for part in parts:
            if "codecs=" in part:
                parts.remove(part)
                break
        return ";".join(parts)

    def handle_video_chunk(self, chunk: str):
        # print("JD", State.get_jd())
        # print("Campany", State.company)
        # print("Got video chunk", len(chunk))
        with self._video_path().open("ab") as f:
            with urlopen(self._strip_codec_part(chunk)) as vid:
                f.write(vid.read())

    def on_stop_recording(self):
        # vapi.stop()
        print(f"Stopped recording: {self._video_path()}")
        self.recording = False

    # vapi.setMuted(true);

    def start_recording(self, ref: str):
        """Start recording a video."""
        return webcam.start_recording(
            ref,
            on_data_available=State.handle_video_chunk,
            on_start=State.on_start_recording,
            on_stop=State.on_stop_recording,
            timeslice=1000,
        )