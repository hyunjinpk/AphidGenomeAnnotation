# GC.py
# See 12June18_assemblystats.txt
# Ref.: https://biopython.org/wiki/SeqIO

from Bio import SeqIO
from Bio.SeqUtils import GC

def main():
  record_dict = SeqIO.to_dict(SeqIO.parse("./dove_scatters.fasta", "fasta"))
  
  seq = ""
  length = 0
  for key in record_dict:
  	seq += record_dict[key]
  	length += len(record_dict[key])

  print(GC(seq))
  print(length)

main()
