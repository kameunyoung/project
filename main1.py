import googletrans
from googletrans import Translator

translator = Translator()

str1 = '파이썬 프로젝트 내용입니다.'
result1 = translator.translate(str1, dest='en', src='auto')
print(f"{str1} -> {result1.text}")

str2 = 'Working on a new project.'
result2 = translator.translate(str2, dest='ko', src='en')
print(f"{str2} -> {result2.text}")
