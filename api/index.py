from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
import pandas as pd
import io
import json

app = Flask(__name__)

def verify_api_key(api_key):
    return api_key == "TESTAPI"

@app.route('/plot', methods=['POST'])
def plot_graph():
    # Check if the request is multipart/form-data or application/json
    if request.content_type.startswith('multipart/form-data'):
        # Handle file upload
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Read API key from form data
        api_key = request.form.get('api_key')
        if not api_key or not verify_api_key(api_key):
            return jsonify({"error": "Invalid or missing API key"}), 401

        # Read CSV file
        df = pd.read_csv(file)

    elif request.content_type == 'application/json':
        # Handle JSON payload
        data = request.get_json()
        if not data or 'api_key' not in data:
            return jsonify({"error": "Missing API key"}), 400

        api_key = data['api_key']
        if not verify_api_key(api_key):
            return jsonify({"error": "Invalid API key"}), 401

        if 'data' not in data:
            return jsonify({"error": "No data provided in JSON payload"}), 400

        payload = data['data']
        if isinstance(payload, list):
            df = pd.DataFrame(payload[1:], columns=payload[0])
        else:
            return jsonify({"error": "Invalid JSON format"}), 400

    else:
        return jsonify({"error": "Unsupported Media Type"}), 415

    # Plotting the data
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:
        plt.plot(df[df.columns[0]], df[column], label=column)
    plt.xlabel(df.columns[0])
    plt.ylabel('Values')
    plt.title('Graph of Data')
    plt.legend()
    plt.grid(True)

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
