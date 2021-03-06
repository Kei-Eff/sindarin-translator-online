import requests
import logging
from flask import Flask, render_template, request
from translation_cache import Cache
from app_secrets import Secrets


def create_app():
    """Creates and returns a Flask application instance.

    Returns:
        A Flask object
    """
    app = Flask(__name__)
    cache = Cache()
    secrets = Secrets()

    # Set logger
    if __name__ != '__main__':
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    # Get API Key from Parameter Store
    api_key = secrets.get_api_key()

    @app.route("/", methods=["GET", "POST"])
    def translate():
        """The translation endpoint.

        GET:
            Displays the index page.

        POST:
            Translates the text in the form request body.
            Checks cache for existing translations.
            Calls API to translate the given text, if not present in cache.
            Saves new translations to cache.

        Returns:
            The index page.
        """

        if request.method == "GET":
            return render_template("index.html", page_data={})

        # Check for null or whitespace
        message = request.form["message"]

        if message.isspace() or len(message) == 0:
            data = {
                "error_message": "Please enter message to translate"
            }

            return render_template("index.html", page_data=data)

        # Check cache
        item = cache.get_item(message)
        if item is not None:
            app.logger.info('Treebeard: A hit! A fine hit!')

            data = {
                "message": message,
                "translated_message": item['translation']
            }

            return render_template("index.html", page_data=data)

        # Call API
        app.logger.info(f"'{message}' not found, calling API preciousss")
        url = "https://api.funtranslations.com/translate/sindarin.json"

        headers = None

        if api_key is not None:
            app.logger.info('Using API key.')
            headers = {
                'X-Funtranslations-Api-Secret': api_key
            }

        querystring = {
            "text": message
        }

        response = requests.request("POST", url,
                                    data=querystring,
                                    headers=headers)

        response_json = response.json()

        app.logger.info(f"API response: {response_json}")

        # Render error response
        if "error" in response_json:
            error_message = response_json["error"]["message"]

            data = {
                "error_message": error_message
            }

            return render_template("index.html", page_data=data)

        # Save response to cache
        contents = response_json["contents"]
        message = contents["text"]
        translation = contents["translated"]

        cache.save_item(message, translation)
        app.logger.info(f"Saved '{message}' to cache!")

        # Render response
        data = {
            "message": message,
            "translated_message": translation
        }

        return render_template("index.html", page_data=data)

    # Go to 'About' page endpoint
    @app.route("/about", methods=["GET"])
    def get_about_page():
        """The about endpoint.

        Returns:
            The about page.
        """
        return render_template("about.html")

    return app
