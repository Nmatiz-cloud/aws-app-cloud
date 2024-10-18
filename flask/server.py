from flask import Flask

app= Flask(__name__)

from routes.route import *

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = "80"
    app.run(ip, port, debug=True)