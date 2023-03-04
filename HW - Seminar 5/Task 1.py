# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'АБВ шрщ enohoh  jk абвогри?  АбВорр ioh! АБВ ор ршр абвбвба'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)