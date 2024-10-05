# TUGAS 2 Sister

This project is a web application that demonstrates the functionality of MQTT (Message Queuing Telemetry Transport) and request-response communication using Flask and JavaScript. The application allows users to interact with MQTT clients, send messages, and handle responses through a simple web interface.

## Features

- **MQTT Client**: Interact with MQTT brokers to publish and subscribe to topics.
- **Request-Response Communication**: Send messages and receive responses from the server, including latency measurements.

## Technology Stack

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Python (Flask)
- **MQTT Library**: Paho MQTT JavaScript Client

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Node.js (for running local development tools, optional)

### Clone the Repository

```bash
git clone https://github.com/yourusername/tugas2-sister.git
cd tugas2-sister
```

### Set Up the Backend

1. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Required Packages**:

   ```bash
   pip install Flask
   ```

### Run the Application

1. **Start the Flask Server**:

   ```bash
   python app.py
   ```

   The server will run on `http://0.0.0.0:5000/`.

2. **Open the Frontend**:

   Open your web browser and navigate to `http://localhost:5000/` to access the application.

## Usage

1. **MQTT Section**:
   - Enter your username, topic, and message.
   - Click **Publish** to send a message to the specified MQTT topic.
   - Click **Subscribe** to listen for messages on the specified topic.

2. **Request-Response Section**:
   - Enter your username and message.
   - Click **Send Request** to send a message to the server.
   - The server responds with a greeting and the message you sent, along with latency information.

## Code Overview

- `app.py`: Contains the Flask backend that handles the web server and API requests.
- `index.html`: The main HTML file containing the frontend interface and JavaScript logic for MQTT and request-response functionalities.

## Dependencies

- Tailwind CSS: For styling the frontend.
- Paho MQTT: For MQTT client functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Paho MQTT](https://www.eclipse.org/paho/)
- [Tailwind CSS](https://tailwindcss.com/)
