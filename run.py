import sys, getopt
import extract, convert

def print_usage():
  print('USAGE: <action> [<additional_action_args>] -i <inputfile> -o <outputfile>\nactions: \n  translate: '+
  '\n\t-x\t\t\textract-names - extract all names to a mapping file for translation'+
  '\n\t-c -m <mappingFile>\tconvert - use naming mapping file to translate csv names')

def main(argv):
  inputFile = ''
  outputFile = ''
  mappingFile = ''

  action = ''

  try:
    opts, args = getopt.getopt(argv,"hxci:o:m:")
  except getopt.GetoptError:
    print('Failed parsing command arguments')
    print_usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print_usage()
      sys.exit()
    elif opt == "-i":
      inputFile = arg
    elif opt == "-o":
      outputFile = arg
    elif opt == "-m":
      mappingFile = arg
    elif opt == '-x':
      action = 'extract'
    elif opt == '-c':
      action = 'convert'

  print(inputFile)
  print(outputFile)
  print(mappingFile)

  if(not inputFile or not outputFile or not action or (action == 'convert' and not mappingFile)):
    print_usage()
    sys.exit(2)
  
  if action == 'extract':
    extract.apply(inputFile, outputFile)

  if action == 'convert':
    convert.apply(inputFile, outputFile, mappingFile)

if __name__ == "__main__":
  main(sys.argv[1:])