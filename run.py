# script simple pour lancer la plateforme mirror d'un coup
import uvicorn
import webbrowser
import threading
import time

def ouvrir_navigateur():
    # attend 1.5 seconde que le serveur demarre et ouvre la page web
    time.sleep(1.5)
    webbrowser.open("http://localhost:8006")

if __name__ == "__main__":
    print("------------------------------------------------------------------")
    print(" 🪞  Lancement de MIRROR Platform Media 360° UI on port 8006")
    print(" Ouverture du navigateur sur http://localhost:8006")
    print("------------------------------------------------------------------")
    
    # ouvrir la page automatiquement
    threading.Thread(target=ouvrir_navigateur, daemon=True).start()
    
    # demarrage du serveur web fastapi
    uvicorn.run("mirror_media_platform.api:app", host="127.0.0.1", port=8006, reload=True)
