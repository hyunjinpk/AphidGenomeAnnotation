# 08June2018
# Converts a txt file into csv file

def main():
  infile = open ("./TableS1.txt", "r")
  
  out = ""
  for line in infile:
    line = line.replace("\t", ",")
    if("X" in line):
      out += line

  infile.close()

  csv_file = open("TableS1_Xonly.csv", "w")
  csv_file.write(out)
  csv_file.close()

main()
  

