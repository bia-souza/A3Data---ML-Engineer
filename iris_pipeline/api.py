from flask import Flask, request, jsonify
import joblib
import os
import time

class IrisAPI:
    def __init__(self, model_path='src/iris_pipeline/model.joblib'):
        while not os.path.exists(model_path):
            print("Aguardando o arquivo model.joblib...")
            time.sleep(5)
        self.model = joblib.load(model_path)
        self.app = Flask(__name__)
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/predict', methods=['POST'])
        def predict():
            data = request.get_json()
            features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
            prediction = self.model.predict([features])
            species = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
            result = {'species': species[prediction[0]]}
            return jsonify(result)
    
    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    iris_api = IrisAPI()
    iris_api.run()
