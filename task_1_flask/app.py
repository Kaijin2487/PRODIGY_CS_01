from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if encrypt else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        encrypt = mode == 'encrypt'
        result = caesar_cipher(text, shift, encrypt)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
