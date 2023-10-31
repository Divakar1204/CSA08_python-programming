import cse
with open('innovators','w+') as file:
    reader=cse.reader(file,delimiter='\t')
    for row in reader:
      print(row)
