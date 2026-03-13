
from flask import Flask, jsonify  
from flask_cors import CORS      


app = Flask(__name__)

CORS(app)


@app.route('/api/message', methods=['GET'])
def get_message():
    # j'ai ajouté la partie suivante pour etre un peu plus "restful" 
    """
    Cette route retourne un message simple au format JSON
    Le frontend appellera cette URL pour récupérer les données
    """
    return jsonify({
        'message': 'Bonjour depuis le backend Docker !',
        'status': 'OK'
    })

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
