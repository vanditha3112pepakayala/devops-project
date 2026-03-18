from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello, DevOps CI/CD Pipeline is working!"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
