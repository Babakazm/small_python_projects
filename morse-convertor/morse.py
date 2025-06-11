# morse_converter.py

# 1. Define the Morse code mapping
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def text_to_morse(text):
    """
    Convert a string to Morse code.
    Unrecognized characters are ignored.
    Spaces between words are represented by '/'.
    """
    morse_chars = []
    for char in text.upper():
        if char == ' ':
            morse_chars.append('/')           # Word separator
        elif char in MORSE_CODE_DICT:
            morse_chars.append(MORSE_CODE_DICT[char])
        # else: ignore punctuation or unknown symbols
    return ' '.join(morse_chars)

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter text to convert to Morse code: ")
    morse = text_to_morse(user_input)
    print(f"Morse Code:\n{morse}")