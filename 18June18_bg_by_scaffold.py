# bg_by_scaffold.py
# See 18June18_bedtools_awk.txt for its purpose.

import csv
import collections

def main():
  # Reads bedtools -bg output and save as 2-D list.
  # https://stackoverflow.com/questions/7856296/parsing-csv-tab-delimited-txt-file-with-python
  infile = open("bedtools_output_bg.txt", "r")
  entries = list(csv.reader(infile, delimiter = "\t"))
  infile.close()
  
  # Each row is [scaffold, start, end, depth]
  # We want dictionary {scaffold: [length, total depth]}
  scaffold = {}
  for row in entries:
  	if row[0] not in scaffold:
  	  len_row = int(row[2]) - int(row[1])
  	  depth_row = len_row * int(row[3])
  	  scaffold[row[0]] = [len_row, depth_row]
  	else:
  	  len_row = int(row[2]) - int(row[1])
  	  depth_row = len_row * int(row[3])
  	  scaffold[row[0]][0] += len_row
  	  scaffold[row[0]][1] += depth_row
  
  # OrderedDict method of "collections" library allows sorting dictionary.
  # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
  od = collections.OrderedDict(sorted(scaffold.items()))

  out_string = "# Divide total_depth by len to attain avg_depth\n# scaffold\tlen\ttotal_depth"
  for k, v in scaffold:
  	out_string = out_string + str(k) + "\t" + str(v[0]) + "\t" + str(v[1]) + "\n"

  outfile = open("./bedtools_output_bg_by_scaffolds.txt", "w")
  outfile.write(out_string)
  outfile.close()

main()