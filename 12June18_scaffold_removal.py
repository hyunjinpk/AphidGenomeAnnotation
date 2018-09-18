# scaffold_removal
# Purpose: removes designated scaffolds

from Bio import SeqIO

def main():
  short = []
  for record in SeqIO.parse("dove_whole.fasta", "fasta"):
  	if len(record.seq) < 40000000:
  	  short.append(record)
  print("Found %i short sequences" % len(short))

  SeqIO.write(short, "dove_scatters.fasta", "fasta")

main()