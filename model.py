import tensorflow as tf
import numpy as np

def load_model(model_path):
    # Cargar el modelo TFLite
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def predict_category(interpreter, audio):
    # Preparar el audio para ser compatible con el modelo
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Asumimos que el audio ya es una muestra de 3 segundos (48,000 muestras)
    audio = np.array(audio, dtype=np.float32)
    audio = np.expand_dims(audio, axis=0)

    # Ejecutar la predicción
    interpreter.set_tensor(input_details[0]['index'], audio)
    interpreter.invoke()

    # Obtener los resultados
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_label = np.argmax(output_data)
    
    return predicted_label
