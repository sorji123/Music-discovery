import os
from flask import Flask, render_template
import main
import imp

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

print("Hello world!")


@app.route("/")  # Python decorator
def hello_world():
    """ Returns root endpoint HTML """

    return render_template(
        "index.html",
        names2=main.names,
        topurl2=main.topurl,
        toptrack2=main.toptrack,
        songurl2=main.songurl,
        imageurl2=main.imageurl



    )


app.run(
    debug=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv("PORT", 8080)))
