# perc_genic.py
# See 12June18_assemblystats.txt

import re

def main():
  infile = open("./dove_3_21646.gff", "r")
  gene_pattern = re.compile("gene=LOC[0-9]+;")
  exon_pattern = re.compile("exon\t([0-9]+)\t([0-9]+)")
  
  total_gene_matches = 0
  total_exon_length = 0

  unique_genes = {}
  for line in infile:
  	if "exon" in line:
  	  gene_match = gene_pattern.search(line)
  	  if gene_match != None:
  	    unique_genes[gene_match.group(0)] = []

  for line in infile:
    if "exon" in line:
      exon_match = exon_pattern.search(line)
      gene_match = gene_pattern.search(line)
      if gene_match != None and exon_match != None:
        gene_key = gene_match.group(0)
        unique_genes[gene_key].append(exon_match.group(1))
        unique_genes[gene_key].append(exon_match.group(2))

  total_genic_length = 0
  for key in unique_genes:
  	min_instance = int(min(unique_genes[key]))
  	max_instance = int(max(unique_genes[key]))
  	if max_instance > min_instance and max_instance < min_instance+567200:
  	  length_instance = max_instance - min_instance
  	else:
  	  length_instance = 0
  	total_genic_length += length_instance
  	print(key, min_instance, max_instance, length_instance, total_genic_length)

  print("Total genic length in chr 3:", total_genic_length)


  
"""
      if gene_match != None:
        total_gene_matches += 1
        if gene_match.group(0) not in unique_genes:
          unique_genes[gene_match.group(0)] = []
          unique_genes[gene_match.group(0)].append(int(exon_match.group(2)))
          unique_genes[gene_match.group(0)].append(int(exon_match.group(1)))
          print(unique_genes[gene_match.group(0)])
        else:
          unique_genes[gene_match.group(0)].append(int(exon_match.group(2)))
          unique_genes[gene_match.group(0)].append(int(exon_match.group(1)))
          print(unique_genes[gene_match.group(0)])
  
  infile.close()

  print("# of exons in chr 3:", len(unique_genes))
  print("Sum exon lengths in chr 3", total_exon_length)
  print("Average exon lengths in chr 3", total_exon_length / len(unique_genes)) """

main()
