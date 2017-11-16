from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
        <!-- create your form here -->
        <form method='POST'>
            <label>Rotate by:
                <input type="text" name="rot" value="0">
            </label>
            <br />
            <textarea name="text">{0}</textarea>
            <br />
            <input type="submit">
        </body>
    </html>
    """

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

    

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encrypted_string = ''

    if is_integer(rot):
        rot = int(rot)
        encrypted_string = (rotate_string(text,rot))
    else:
        encrypted_string = 'Please enter a valid integer into the Rotate By input box'
        rot = ''

    return form.format(encrypted_string)



app.run()