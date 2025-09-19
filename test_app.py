# test_app.py

import unittest
import json
from app import app  # Importiert die Flask-App-Instanz aus unserer app.py-Datei

class SimpleApiTest(unittest.TestCase):
    """
    Test-Suite für unsere einfache Flask-API.
    """

    def setUp(self):
        """
        Diese Methode wird vor jedem einzelnen Test aufgerufen.
        Hier richten wir einen Test-Client für unsere App ein.
        """
        self.app = app.test_client()
        # Aktiviert den Testmodus, um Fehler besser sichtbar zu machen.
        self.app.testing = True

    def test_home_status_code(self):
        """
        Testet, ob der Endpunkt '/' einen erfolgreichen Status-Code 200 zurückgibt.
        """
        # Sendet eine GET-Anfrage an den Endpunkt '/'
        response = self.app.get('/')
        # Überprüft, ob der Status-Code der Antwort 200 (OK) ist.
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        """
        Testet, ob die zurückgegebenen Daten die erwartete Nachricht enthalten.
        """
        # Sendet eine GET-Anfrage an den Endpunkt '/'
        response = self.app.get('/')
        # Wandelt die JSON-Antwort von Bytes in ein Python-Dictionary um.
        data = json.loads(response.get_data(as_text=True))
        # Überprüft, ob der Wert des Schlüssels 'message' korrekt ist.
        self.assertEqual(data['message'], 'Hallo CI/CD Pipeline!')

# Dieser Block ermöglicht es, die Tests direkt über die Kommandozeile auszuführen.
if __name__ == '__main__':
    unittest.main()