from flask import Flask, send_from_directory
import sys

app = Flask(__name__, static_url_path='')

f_name = ""


@app.route('/')
def get_file():
    return send_from_directory('.', f_name)


@app.route('/name')
def get_file_name():
    return f_name


if __name__ == "__main__":
    f_name = sys.argv[1]
    print (f_name)
    app.run("0.0.0.0", "1921")
