from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello,I love you"


if __name__ == "__main__":
    # 127.0.0.1 本机回环地址
    app.run(host="0.0.0.0", debug=True)
    # app.run()
