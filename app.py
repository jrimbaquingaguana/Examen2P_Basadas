from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Cargar el pipeline completo (modelo + scaler)
pipeline = joblib.load('model.pkl')

# Lista de claves esperadas
expected_keys = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
                'marital-status', 'occupation', 'relationship', 'race', 'sex', 
                'capital-gain', 'capital-loss', 'hours-per-week', 'country']

def validate_input(data):
    # Validar que todas las claves esperadas están presentes
    missing_keys = [key for key in expected_keys if key not in data]
    if missing_keys:
        return f'Missing keys: {", ".join(missing_keys)}', False
    
    # Validar que los valores son del tipo correcto (numérico en este caso)
    for key in expected_keys:
        if key in data:
            try:
                # Convertir el valor a float
                float(data[key])
            except ValueError:
                return f'Invalid value for {key}: must be a number', False

    return None, True

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        
        # Validar la entrada
        error_message, is_valid = validate_input(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        # Crear un DataFrame con los datos de entrada
        input_data = pd.DataFrame([data], columns=expected_keys)
        
        # Aplicar el pipeline para obtener la predicción
        prediction = pipeline.predict(input_data)
        
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def serve_index():
    return send_from_directory('web', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('web', path)

if __name__ == '__main__':
    app.run(debug=True)
