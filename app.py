# app.py

from flask import Flask, jsonify

# Erstellt eine Instanz der Flask-Anwendung
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    Dieser Endpunkt gibt eine einfache JSON-Nachricht zurück.
    """
    # jsonify wandelt das Python-Dictionary automatisch
    # in eine JSON-Antwort mit dem korrekten Content-Type-Header um.
    return jsonify({"message": "Hallo CI/CD Pipeline!"})

# Dieser Block stellt sicher, dass der Server nur gestartet wird,
# wenn das Skript direkt ausgeführt wird (und nicht, wenn es importiert wird).
if __name__ == '__main__':
    # Startet die Anwendung auf dem lokalen Entwicklungsserver.
    # debug=True sorgt dafür, dass der Server bei Code-Änderungen neu startet.
    app.run(debug=True)