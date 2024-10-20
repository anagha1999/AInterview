import reflex as rx
import time
from pathlib import Path
from urllib.request import urlopen
from PIL import Image
import reflex_webcam as webcam
# from vapi_python import Vapi
from ..backend.backend import State

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

class CameraState(rx.State):
    last_screenshot: Image.Image | None = None
    last_screenshot_timestamp: str = ""
    loading: bool = False
    recording: bool = False

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
            on_data_available=CameraState.handle_video_chunk,
            on_start=CameraState.on_start_recording,
            on_stop=CameraState.on_stop_recording,
            timeslice=1000,
        )


def last_screenshot_widget() -> rx.Component:
    """Widget for displaying the last screenshot and timestamp."""
    return rx.box(
        rx.cond(
            CameraState.last_screenshot,
            rx.fragment(
                rx.image(src=CameraState.last_screenshot),
                rx.text(CameraState.last_screenshot_timestamp),
            ),
            rx.center(
                rx.text("Click image to capture.", size="4"),
            ),
        ),
        height="270px",
    )


def webcam_upload_component(ref: str) -> rx.Component:
    """Component for displaying webcam preview and uploading screenshots.
    Args:
        ref: The ref of the webcam component.
    Returns:
        A reflex component.
    """
    return rx.vstack(
        webcam.webcam(
            id=ref,
            on_click=webcam.upload_screenshot(
                ref=ref,
                handler=CameraState.handle_screenshot,  # type: ignore
            ),
            audio=True,
        ),
        rx.cond(
            ~CameraState.recording,
            rx.button(
                "🟢 Start Recording",
                on_click=CameraState.start_recording(ref),
                color_scheme="green",
                size="4",
            ),
            rx.button(
                "🟤 Stop Recording",
                on_click=webcam.stop_recording(ref),
                color_scheme="tomato",
                size="4",
            ),
        ),
        rx.cond(
            CameraState.video_exists,
            rx.link(
                "Download Last Video", href=rx.get_upload_url(VIDEO_FILE_NAME), size="4"
            ),
        ),

        width="1000px",
        align="center",
    )
