""" Translation logic """
import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

# Prepare the Authenticator
translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=IAMAuthenticator(apikey)
)
translator.set_service_url(url)

# make the translation funcitons
def english_to_french(english_text):
    """Translate English into French"""
    translation = translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """Translate French into English"""
    translation = translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
