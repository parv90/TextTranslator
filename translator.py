from os import write
from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('./translate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test_ja.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print(f'check your file path {e}')