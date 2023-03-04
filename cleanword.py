Cad_name = 'BDE84572.002-2458 VFI(FUEL-Cap)___8426'
# clean CAD name
def Uppercase(text):
    return text.upper()

def removePunctuation(text):
    punctuations = '.-,* _()'
    for punctuation in punctuations:
        text = text.replace(punctuation, '_')
    return text

def removeextra_(text):
    list1 = text.split('_')
    while("" in list1):
        list1.remove("")
    return '_'.join(str(cleanword) for cleanword in list1)

cleanName = [Uppercase, removePunctuation, removeextra_]

for step in cleanName:
    Cad_name = step(Cad_name)

print(str(Cad_name))