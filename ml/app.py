from flask import Flask, request, jsonify

from predict import predict


app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def prediction():

    data = request.get_json()

    url = data.get("url")

    if not url:
        return jsonify({
            "error": "URL is required"
        }), 400

    result = predict(url)

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        port=5000,
        debug=True
    )