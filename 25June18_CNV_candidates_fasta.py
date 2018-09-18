# 25June18_CNV_candidates_fasta.py
# See 25June18_CNV.txt
# See BioPython SeqIO documentation: https://biopython.org/wiki/SeqIO

from Bio import SeqIO

def final_candidates(CNV_summary_infile):
  candidates = []
  for line in CNV_summary_infile:
  	col = line.split("\t")
  	if int(col[1]) == 0:
  	  candidates.append(col[0])
  	  print(col[0])
  return candidates

def make_fasta(candidates):
  infile = "pea_aphid_24Feb2018_fmGlB.fasta"
  records = SeqIO.to_dict(SeqIO.parse(infile, "fasta"))
  out_record = {}
  for key in records:
  	if key in candidates:
  	  out_record[key] = records[key]
  return out_record

def main():
  # read CNV_summary
  CNV_summary_infile = open("CNV_summary.txt", "r")

  # get scaffolds with zero SNPs/indels/MNPs, etc.
  # these are the final 32 candidate scaffolds
  candidates = final_candidates(CNV_summary_infile)
  CNV_summary_infile.close()

  # with biopython, generate fasta file
  records= make_fasta(candidates)
  print(records)

  # write outfile
  outstring = ""
  for key in records:
  	outstring = outstring + ">" + key + "\n" + records[key]

  outfile = open("25June18_CNV_candidates.fasta", "w")
  outfile.write(outstring)
  outfile.close()

main()

# scp ./25June18_CNV_candidates_fasta.py hyunjin@ochmcomp01.ccbb.utexas.edu:/stor/work/Ochman/hyunjin/data/genomes/dovetail