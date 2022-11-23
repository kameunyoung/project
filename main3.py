import googletrans
from googletrans import Translator
import time

translator = Translator()

str1 = r"C:\Users\mit\Desktop\project\project_trans\the_old_town.txt"
str2 = r"C:\Users\mit\Desktop\project\project_trans\the_old_town_ko.txt"

with open(str1, 'r', encoding='UTF-8') as f:
    readLines = f.readlines()

for lines in readLines:
    result = translator.translate(lines, dest='ko')
    print(result.text)
    time.sleep(0.5)
    with open(str2, 'a', encoding='UTF-8') as f:
        f.write(result.text + '\n')
