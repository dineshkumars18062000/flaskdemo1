from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello, World!</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    </head>
    <body class="container mt-5">
        <div class="jumbotron text-center">
            <h1 class="display-4">Hello, World!</h1>
            <p class="lead">This is a simple Flask app.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)