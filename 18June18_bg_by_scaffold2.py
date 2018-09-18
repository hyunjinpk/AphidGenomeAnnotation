# bg_by_scaffold2.py
# See 18June18_bedtools_awk.txt for its purpose.

import csv

def main():
  # Reads bedtools -bg output and save as 2-D list.
  # https://stackoverflow.com/questions/7856296/parsing-csv-tab-delimited-txt-file-with-python
  infile = open("bedtools_output_1000.txt", "r")
  entries = list(csv.reader(infile, delimiter = "\t"))
  infile.close()

  for row in entries:
  	row[2] = int(row[2]) / int(row[1])
  
  # Write the list out as a .csv file
  out_string = ""
  for row in entries:
  	out_string = out_string + str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "\n"

  outfile = open("./bedtools_output_avg.csv", "w")
  outfile.write(out_string)
  outfile.close()


main()