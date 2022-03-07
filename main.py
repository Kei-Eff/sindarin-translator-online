import json
import requests
from flask import Flask, render_template, request

def create_app():

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def translate():

        if request.method == "GET":
            return render_template("index.html", page_data={})

        url = "https://api.funtranslations.com/translate/sindarin.json"
    
        querystring = {
            "text": request.form["message"]
        }

        # response = requests.request("POST", url, data=querystring)
    
        # response_json = response.json()

        response_json = json.loads("{\"error\":{\"message\":\"Too many requests\"}}")

        if "error" in response_json:
            error_message = response_json["error"]["message"]
            
            data = {
                "error_message": error_message
            }

            return render_template("index.html", page_data=data)
        else:
            contents = response_json["contents"]
            message = contents["text"]
            translation = contents["translated"]
            
            data = {
                "message": message,
                "translated_message": translation
            }

            return render_template("index.html", page_data=data)

    return app