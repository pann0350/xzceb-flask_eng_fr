import json

from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench(request):
    text_to_translate = request.args.get("textToTranslate")
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text


@app.route("/frenchToEnglish")
def frenchToEnglish(request):
    text_to_translate = request.args.get("textToTranslate")
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text


@app.route("/")
def renderIndexPage(request):
    return render_template(request, "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
