from flask import Flask, jsonify, request
from services.ConvertVideoService import convert_video, convert_many_videos

app = Flask(__name__)  

@app.route('/convert', methods=['POST'])
def convert_video_endpoint():
    data = request.get_json()
    if not data or 'directorio' not in data:
        return jsonify({'error': 'No directory provided'}), 400

    directorio = data['directorio']
    resultado = convert_video(directorio)
    
    if "Error" in resultado:
        return jsonify({'error': resultado}), 500
    
    return jsonify({'message': 'Video converted successfully', 'result': resultado}), 200


@app.route('/convertFolder', methods=['POST'])
def convert_many_video_endpoint():
    data = request.get_json()
    if not data or 'directorio' not in data:
        return jsonify({'error': 'No directory provided'}), 400

    directorio = data['directorio']
    resultado = convert_many_videos(directorio)
    
    if "Error" in resultado:
        return jsonify({'error': resultado}), 500
    
    return jsonify({'message': 'Video converted successfully', 'result': resultado}), 200