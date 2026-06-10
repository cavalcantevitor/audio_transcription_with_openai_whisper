import whisper
from pydub import AudioSegment
from pathlib import Path

BASE_DIR = Path.cwd()
AUDIO_DIR = BASE_DIR / "audio"
RAW_AUDIO_DIR = AUDIO_DIR / "raw"
CONVERTED_AUDIO_DIR = AUDIO_DIR / "converted"

FILE = "WhatsApp Ptt 2026-06-09 at 20.55.13.ogg"
FILE_PATH = RAW_AUDIO_DIR / FILE

# Converting the audio file into the supported formats
supported_formats = [".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".ogg", ".wav", ".webm"]
if FILE_PATH.suffix.lower() not in supported_formats:
    TRANSCRIBE_PATH = CONVERTED_AUDIO_DIR / f"{FILE_PATH.name}.mp3"
    audio = AudioSegment.from_file(FILE_PATH)
    audio.export(TRANSCRIBE_PATH, format="mp3")
else:
    TRANSCRIBE_PATH = FILE_PATH

# Transcribing the audio file
model = whisper.load_model("base")
result = model.transcribe(str(TRANSCRIBE_PATH))
print(type(result["text"]))
