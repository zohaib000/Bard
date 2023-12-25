from flask import Flask, request, jsonify
from bardapi import Bard
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Replace the token with your actual Bard API token
bard = Bard(token="eghO3gndGv_OdaBxIRMJUqz8RML8YWfRXDGGmM7DZGBiILHmtlwjrqQmW1ozvT22GeOmoQ.")

@app.route('/get_answer', methods=['POST'])
def get_answer():
    if request.method == 'POST':
        data = request.get_json()  
        query = data.get('query') 
        if query:
            response = bard.get_answer(query)["content"]  
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'No query provided'})
    else:
        return jsonify({'error': 'Invalid request method'})

if __name__ == '__main__':
    app.run(debug=True,port=8000)
