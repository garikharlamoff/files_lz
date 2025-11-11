import docx
d = docx.Document('lion.docx')
t = []
al = ''
k = {}
for i in d.paragraphs:
    t.append(i.text)  
print(t)
ch = [' ']

for i in ch:
    t = t.replace(i, "")

for i in t:                             
    al += i
t = al.split()
print(len(t))                     
for i in t:
    if i in k:
        k[i] += 1
    else:
        k[i] = 1
print('',k['солнце'])
print('',k['солнцу'])
print('москва',k['Москва'])
print('если',k['если'])
print('ну',k['ну'])
print('вот',k['вот'])
print('мир',k['мир'])
print('война',k['война'])
print('и',k['и'])
print('а',k['а'])
print('о',k['о'])