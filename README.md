# Audio-to-Text Whisper

This project provides a simple batch transcription tool using OpenAI's **Whisper** model for speech recognition.  
It automatically converts all audio files (such as `.ogg`, `.mp3`, `.wav`, and `.m4a`) in the current directory into text files with the same base name.

Each audio file is processed and a corresponding `.txt` file containing the transcription is saved in the same folder.

---

## How It Works

The main script [`batch_audio_to_text_whisper.py`](batch_audio_to_text_whisper.py) performs the following steps:

1. Loads a Whisper model (you can choose `tiny`, `base`, `small`, `medium`, or `large`).
2. Scans the current folder for compatible audio files.
3. Transcribes each audio file into text.
4. Saves each transcription as a `.txt` file with the same name.

For example:
```
meeting.ogg  →  meeting.txt
lecture.wav  →  lecture.txt
```
All outputs are saved in the same folder.

---

## Installation & Setup

You can run the project locally without any external API keys or internet access once Whisper and Torch are installed.

### 1. Create a virtual environment
```bash
python -m venv speech
speech\Scripts\activate
```

### 2. Install dependencies
```bash
pip install git+https://github.com/openai/whisper.git
pip install torch tqdm
```

### 3. Place your audio files in the project directory

Supported formats: `.ogg`, `.mp3`, `.wav`, `.m4a`

### 4. Run the script
```bash
python batch_audio_to_text_whisper.py
```

---

## Configuration

Inside the script, you can modify:
```python
MODEL_NAME = "medium"  # tiny, base, small, medium, large
LANG = "pt"            # language code, or None for auto-detect
```

To improve speed, you may select a smaller model like `"small"` or `"base"`.

---

## Output

For each audio file, a text file with the same base name will be created, containing the transcription.

Example output structure:
```
audio1.ogg
audio1.txt
audio2.wav
audio2.txt
```

---

## Notes

- All processing is done **locally**; no data is sent to the cloud.
- Whisper models are multilingual and automatically detect most spoken languages.
- Larger models are slower but more accurate.
- You can freely modify or extend the script to process subfolders or change output behavior.

---

## License

This project uses OpenAI's open-source [Whisper](https://github.com/openai/whisper) model under the MIT License.

---

Developed for research, experimentation, and educational use.
