from flask import Flask, request, jsonify
import os
from preprocess import preprocess_audio
from model import load_model, predict_category

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurarse de que la carpeta de uploads exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Cargar el modelo al iniciar la aplicación
model = load_model('modelo/sirenas_model.tflite')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No se encontró archivo de audio'}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

    # Guardar el archivo
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
    audio_file.save(file_path)

    # Preprocesar el audio
    processed_audio = preprocess_audio(file_path)

    # Realizar la predicción
    category = predict_category(model, processed_audio)

    # Eliminar el archivo después de usarlo
    os.remove(file_path)

    return jsonify({'category': category})

if __name__ == '__main__':
    app.run(debug=True)
