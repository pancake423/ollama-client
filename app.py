from flask import Flask
from subprocess import run
from colors import red, yellow, blue

PORT = 5000

app = Flask(__name__, static_url_path="/")

@app.route("/")
def index():
    return app.send_static_file("index.html")

def check_ollama_started():
    print("searching for ollama on local system...")
    try:
        res = run("ollama -v", shell=True, capture_output=True)
        print(res.stdout.decode("utf-8"))
        run("ollama serve", shell=True, capture_output=True)
        return True
    except:
        print(red("fatal error: ollama is not installed."), "see https://ollama.com/download")

    return False



if __name__ == "__main__":
    # ensure ollama is installed and running
    if not check_ollama_started():
        exit()
    # start the local server
    print("started server at", blue(f"http://localhost:{PORT}"))
    print(yellow("CTRL+C"), "to close.")
    try:
        run(f"uv run flask run --port {PORT}", shell=True, capture_output=True)
    except KeyboardInterrupt:
        print("\nserver closed.")
