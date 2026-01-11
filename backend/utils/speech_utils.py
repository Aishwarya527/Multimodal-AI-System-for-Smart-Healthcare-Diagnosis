import whisper
import tempfile

speech_model = whisper.load_model("base")

def speech_to_text(audio_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio_file.save(tmp.name)
        result = speech_model.transcribe(tmp.name)
    return result["text"]
