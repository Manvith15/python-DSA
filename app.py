from flask import Flask
app=Flask(__name__)



@app.route("/")
def hello():
    return"hello "

@app.route("/natural")
def natural_numbers():
    numbers = [str(i) for i in range(1,11)]
    return ",".join(numbers)

if __name__ == "__main__":
    app.run
