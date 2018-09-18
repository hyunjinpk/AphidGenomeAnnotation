# unique_genes.py
# See 12June18_assemblystats.txt
# Regular expression ref.: https://docs.python.org/3/library/re.html
# Regular expression matcher: https://pythex.org/

import re

def main():
  infile = open("./dove_3_21646.gff", "r")
  pattern = re.compile("gene=LOC[0-9]+;")
  
  total_matches = 0
  unique_genes = []
  for line in infile:
    match = pattern.search(line)

    if match != None:
      total_matches += 1
      if match.group(0) not in unique_genes:
        print(match)
        unique_genes.append(match.group(0))
  
  infile.close()
  print("# of total matches in chr 3:", total_matches)
  print("# of unique genes in chr 3:", len(unique_genes))

main()