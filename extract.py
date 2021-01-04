import csv, re
import constants

def read(fp):
  names_set=set()
  with open(fp, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    first=True
    for row in csvreader:
      if not first:
        for index in constants.NAME_FIELDS_INDEX:
          #print(index, '| '.join(row))
          for name in row[index].split(' '):
            names_set.add(name.strip().lower())
      else:
        first=False
  
  #print(', '.join(names_set))
  return names_set

def write_mapping_file(names, fp):
  with open(fp, 'w') as csvfile:
    fieldnames = ['word', 'translation']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for name in names:
      if not re.match(constants.NAMES_FILTER_REGEX, name):
        writer.writerow({'word': name})

def apply(inf, outf):
  print('....')
  names = read(inf)
  write_mapping_file(names,outf)
  print('DONE')