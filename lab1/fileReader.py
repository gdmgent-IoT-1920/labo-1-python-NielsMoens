#Open the file
files= open("E:\\git\\labo-1-python-NielsMoens\\lab1\\namen.txt")
#read the file
txt = files.read()
#split the file into fileObject
content=txt.split()
# count dif names in file
print('Olivier komt', content.count('Olivier'), 'keer voor in de file')
print('Frederick komt', content.count('Frederick'), 'keer voor in de file')
print('Evelien komt', content.count('Evelien'), 'keer voor in de file')