# bg_by_scaffold.py
# See 18June18_bedtools_awk.txt for its purpose.

import csv
import collections

def main():
  # Reads bedtools -bg output and save as 2-D list.
  # https://stackoverflow.com/questions/7856296/parsing-csv-tab-delimited-txt-file-with-python
  # Original input on 18June18: "bedtools_output_bg.txt"
  infile = open("03July18_bedtools_RepeatMaskedoutput_bg.txt", "r")
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
  
  # Sorting a dictionary: https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
  out_string = "# Divide total_depth by len to attain avg_depth\n# scaffold\tlen\ttotal_depth\tavg_depth\n"
  for key in sorted(scaffold):
  	out_string = out_string + str(key) + "\t" + str(scaffold[key][0]) + "\t" + str(scaffold[key][1]) + "\t" + str(scaffold[key][1] / scaffold[key][0]) + "\n"
  
  # Original output on 18June18: "./bedtools_output_bg_by_scaffolds_v2.txt" > "bedtools_output_bg.txt"
  outfile = open("03July18_bedtools_RepeatMaskedoutput_bg_by_scaffold_output.txt", "w")
  outfile.write(out_string)
  outfile.close()

main()