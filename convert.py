import csv
import constants

def apply(inf, outf, mapf):
  print('....')
  # read mapping file
  map_dict={}
  with open(mapf, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    first=True
    for row in csvreader:
      if not first:
        if not row[1]:
          print('WARN: no mapping for '+row[0])
        else:
          map_dict[row[0]] = row[1]    
      else:
        first=False

  print(map_dict)
  # convert all name and save them to out file
  new_csv=''
  with open(inf, 'r') as inFile:
    new_csv=inFile.read()
    for name in map_dict:
      new_csv=new_csv.replace(name, map_dict[name])
    
    with open(outf, 'w') as outFile:
      outFile.write(new_csv)
  
  print('DONE')