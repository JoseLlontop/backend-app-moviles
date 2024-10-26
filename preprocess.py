import librosa
import numpy as np

def preprocess_audio(file_path):
    # Cargar el archivo de audio (asumiendo 3 segundos, 16 kHz)
    audio, sr = librosa.load(file_path, sr=16000)
    audio, _ = librosa.effects.trim(audio, top_db=20)  # Eliminar silencios
    if len(audio) < 3 * 16000:
        # Asegurarse de que el audio tenga exactamente 3 segundos
        audio = np.pad(audio, (0, 3 * 16000 - len(audio)))
    return audio