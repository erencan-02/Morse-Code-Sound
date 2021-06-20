import winsound
import json
import time



TIME_UNIT = 200 #ms
FREQUENCY = 1000



def play_morse_code(text=None, file_path=None, TIME_UNIT=200, FREQUENCY=1000):
    if text:
        words = [i.strip().split(' ') for i in text.split('\n')]
    elif file_path:
        words = [i.strip().split(' ') for i in open('text.txt', 'r').readlines()]
    else:
        raise ValueError('No text or file specified')


    with open('translator.json', 'r') as file:
        translator = json.load(file)


    for row in words:
        for word in row:
            print(f'new word: {word}')
            for char in word:
                char_morse_code = translator[char.lower()]
                print(char, char_morse_code)

                for char in char_morse_code:
                    winsound.Beep(FREQUENCY, (1 if char == '.' else 3)*TIME_UNIT)
                    time.sleep(TIME_UNIT/1000)
                time.sleep((TIME_UNIT*3)/1000)
            time.sleep((TIME_UNIT*7)/1000)



#play_morse_code(text='sos', TIME_UNIT=150, FREQUENCY=500)
