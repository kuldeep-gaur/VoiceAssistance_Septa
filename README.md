# VoiceAssistance_Septa

A simple Python-based voice assistant that listens for the activation word **"septa"** and executes basic commands such as opening popular websites or playing music from a predefined library.

## Features

- **Voice Activation:** Listens for the activation word "septa" to start processing commands.
- **Web Commands:** Opens Google, YouTube, Facebook, Twitter, or Instagram by voice command.
- **Music Playback:** Plays music from a user-defined library (see `MusicLibrary` module).
- **Text-to-Speech:** Provides spoken feedback using text-to-speech.
- **Extensible:** Easily add more commands or extend functionality.

## Requirements

- Python 3.8–3.10 (recommended for compatibility)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywin32](https://pypi.org/project/pywin32/) (for Windows)
- Microphone

- ## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/<your-username>/VoiceAssistance_Septa.git
   cd VoiceAssistance_Septa
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
If you don’t have a `requirements.txt`, install manually:
   ```sh
   pip install SpeechRecognition pyttsx3 pywin32
   ```

4. **Ensure your microphone is connected and working.**

## Usage

Run the main script:

```sh
python Main.py
```

- The assistant will listen for the activation word **"septa"**.
- After activation, speak a command such as:
  - "open google"
  - "open youtube"
  - "open facebook"
  - "open twitter"
  - "open instagram"
  - "play [songname]" (where `[songname]` is a key in your `MusicLibrary.music` dictionary)

## Customizing Music Library

Edit the `MusicLibrary.py` file to add or update your music links.  
Example:
```python
# MusicLibrary.py
music = {
    "song1": "https://link-to-song1.com",
    "song2": "https://link-to-song2.com"
}
```

## Example Commands

- **"septa"** (to activate)
- **"open google"**
- **"play song1"**

## Troubleshooting

- If you get `ModuleNotFoundError: No module named 'pythoncom'`, install `pywin32`:
  ```sh
  pip install pywin32
  ```
  - Make sure you are using the correct Python version and virtual environment.
- Ensure your microphone is not muted and is set as the default input device.

## License

This project is for educational purposes.

---

**Contributions are welcome!**
