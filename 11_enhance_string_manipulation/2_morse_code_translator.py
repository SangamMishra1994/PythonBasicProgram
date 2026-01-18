# morse code dictionary

MORSE_CODE_DICT = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_code_decoder(morse_code):
    if not morse_code or not morse_code.strip():
        return ""
    decoded_message = []

    words = morse_code.strip().split(" / ")

    for word in words:
        letters = word.split()
        decoded_word = []

        for symbol in letters:
            decoded_char = MORSE_CODE_DICT.get(symbol, "?")
            decoded_word.append(decoded_char)

        decoded_message.append("".join(decoded_word))

    return " ".join(decoded_message)


print(morse_code_decoder(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
print(morse_code_decoder(""))
print(morse_code_decoder("ABCDE"))
