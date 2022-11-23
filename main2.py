import googletrans
from googletrans import Translator
import time

translator = Translator()

str = r"C:\Users\mit\Desktop\project\project_trans\the_old_town.txt"

with open(str, 'r', encoding='UTF-8') as f:
    readLines = f.readlines()

for lines in readLines:
    result = translator.translate(lines, dest='ko')
    print(result.text)
    time.sleep(0.5)
