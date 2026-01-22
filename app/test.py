from dotenv import load_dotenv
import os

# Charger les variables du fichier .env
load_dotenv() 

# Maintenant, votre code original fonctionnera
token = os.environ.get("HF_TOKEN")
print(f"HF_TOKEN défini: {token is not None}")
print(f"Token: {token[:10]}..." if token else "Non trouvé")