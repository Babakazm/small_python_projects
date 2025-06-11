from flask import Flask, render_template, request
# your existing mapping & function
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-','V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--','Z': '--..',
    '0': '-----','1': '.----','2': '..---','3': '...--',
    '4': '....-','5': '.....','6': '-....','7': '--...',
    '8': '---..','9': '----.'
}

def text_to_morse(text):
    morse_chars = []
    for char in text.upper():
        if char == ' ':
            morse_chars.append('/')
        elif char in MORSE_CODE_DICT:
            morse_chars.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_chars)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        user_text = request.form.get('text', '')
        result = text_to_morse(user_text)
    return render_template('index.html', morse=result)

if __name__ == '__main__':
    app.run(debug=True)