# Audio Transcription with Whisper

Small Python project for transcribing local audio files with OpenAI Whisper.

The script reads an audio file from `audio/raw/`, converts it to `.mp3` when the original format is not directly supported, and saves the transcription as a `.txt` file in `transcripts/`.

## Project Structure

```text
.
├── audio/
│   ├── converted/
│   └── raw/
├── .gitignore
├── transcripts/
├── main.py
└── requirements.txt
```

Folder purpose:

- `audio/raw/`: original audio files.
- `audio/converted/`: audio files generated during conversion.
- `transcripts/`: saved transcription text files.

Audio files, generated transcript `.txt` files, virtual environments, and Python cache files are ignored by git. `.gitkeep` files keep the empty project folders available in git.

## Installation

This project needs Python 3, the packages in `requirements.txt`, and `ffmpeg`.

### Windows

Create and activate a virtual environment:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Install `ffmpeg` with Winget:

```powershell
winget install Gyan.FFmpeg
```

If PowerShell blocks virtual environment activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Linux

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install `ffmpeg`.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Fedora:

```bash
sudo dnf install ffmpeg
```

### macOS

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install `ffmpeg` with Homebrew:

```bash
brew install ffmpeg
```

### Verify ffmpeg

```bash
ffmpeg -version
```

If that command prints version information, `ffmpeg` is available to the project.

## Usage

Put source audio files in:

```text
audio/raw/
```

Update the `FILE` value in `main.py` with the audio filename:

```python
FILE = "your-audio-file.ogg"
```

Run the script:

```bash
python main.py
```

The script loads the Whisper `base` model and saves the transcription to:

```text
transcripts/transcription_your-audio-file.txt
```

## Supported Input Formats

The script treats these formats as supported by Whisper:

```text
.mp3, .mp4, .mpeg, .mpga, .m4a, .ogg, .wav, .webm
```

Other formats are converted to `.mp3` in `audio/converted/` before transcription.
