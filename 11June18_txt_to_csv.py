# 08June2018
# Converts a txt file into csv file
# See 11June18_Jaquiery.txt for its purpose.

def main():
  infile = open ("./NCBI_name_conversion.txt", "r")
  
  out = ""
  for line in infile:
    line = line.replace("\t", ",")
    out += line

  infile.close()

  csv_file = open("NCBI_name_conversion.csv", "w")
  csv_file.write(out)
  csv_file.close()

main()
  

