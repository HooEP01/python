from translate import Translator

try:
    with open('file/test.txt', mode='r') as my_file:
        translator= Translator(to_lang="zh")
        translation = translator.translate(my_file.read())
        print(translation)
        with open('file/test-zh.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('file does not exist')