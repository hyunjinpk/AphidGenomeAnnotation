# avg_exon_length.py
# See 12June18_assemblystats.txt
# Regular expression ref.: https://docs.python.org/3/library/re.html
# Regular expression matcher: https://pythex.org/

import re

def main():
  infile = open("./dove_X_21646.gff", "r")
  pattern = re.compile("exon\t([0-9]+)\t([0-9]+)")
  
  total_matches = 0
  total_exon_length = 0
  unique_genes = []
  for line in infile:
    if "exon" in line:
      match = pattern.search(line)

      if match != None:
        total_matches += 1
        if match.group(0) not in unique_genes:
          unique_genes.append(match.group(0))
          # This was stupid. Add 1 to the average exon lengths output.
          instance_exon_length = int(match.group(2)) - int(match.group(1))
          total_exon_length += instance_exon_length
  
  infile.close()

  print("# of exons in chr 3:", len(unique_genes))
  print("Sum exon lengths in chr 3", total_exon_length)
  print("Average exon lengths in chr 3", total_exon_length / len(unique_genes))

main()



