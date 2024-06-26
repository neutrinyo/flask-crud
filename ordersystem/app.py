from . import create_app
import os

print(os.getenv("CONFIG_MODE"))
app = create_app(os.getenv("CONFIG_MODE"))

@app.route("/")
def hello():
    return "Hello!"

from . import urls

if __name__ == "__main__":
    app.run()