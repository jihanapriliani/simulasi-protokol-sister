from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send-request", methods=["POST"])
def send_request():
    start_time = time.time()
    data = request.get_json()
    username = data.get("username")
    message = data.get("message")

    if username and message:
        # Simulasi latensi server
        time.sleep(0.5)  # Simulated server processing time

        response_data = {
            "response": f"Hello, {username}! You sent: {message}",
            "server_latency": (time.time() - start_time) * 1000,  # Simulated server latency in milliseconds
        }
        return jsonify(response_data)
    else:
        return jsonify({"error": "Invalid request"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
