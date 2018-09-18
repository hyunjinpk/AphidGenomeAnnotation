# 25June18_CNV.py
# See 25June18_CNV.txt.

import re

def filter_by_degenerate(ref_bases):
  # N is a degenerate nucleotied (can be A, T, C, or G)
  # if reference is a string of N's, return true
  # else, return false
  pattern = re.compile("N+")
  result = pattern.match(ref_bases)
  return result

def is_candidate(cand, scaffold_name):
  # candidate scaffolds were previously determined by read depth analysis
  # See
  # Read depth 6-10, inclusive
  return scaffold_name in cand

def main():
  # read vcf file
  vcf_infile = open("output_freebayes_qual20.vcf", "r")

  # read candidates
  candidates = open("CNV_candidates_depth.txt", "r")
  cand = ""
  for line in candidates:
  	line = line.strip()
  	cand += line
  candidates.close()

  # filter
  # see comments in respective functions for details
  candidates_round_two = ""
  for line in vcf_infile:
  	if line[0] == "#":
  	  continue
  	columns = line.split("\t")
  	if filter_by_degenerate(columns[3]):
  	  continue
  	elif is_candidate(cand, columns[0]):
  	  candidates_round_two += line
  vcf_infile.close()

  # write to outfile
  outfile = open("CNV_candidates_depth_and_SNPs.vcf", "w")
  outfile.write(candidates_round_two)
  outfile.close()

main()

