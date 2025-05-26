import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn="https://c7816add9e1482a0ab527e56f3410282@o4509388551028736.ingest.us.sentry.io/4509388559024128",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the homepage! Try /slow or /fast or /crash"

@app.route("/slow")
def slow_function():
    import time
    time.sleep(0.1)
    return "slow done"

@app.route("/fast")
def fast_function():
    import time
    time.sleep(0.05)
    return "fast done"

@app.route("/crash")
def crash():
    1 / 0  # This will raise ZeroDivisionError

if __name__ == "__main__":
    app.run(debug=True)