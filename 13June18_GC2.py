# GC2.py
# See 12June18_assemblystats.txt
# Purpose: to count %GC of dove_scatters.fasta

def main():
  infile = open("./dove_1.fasta", "r")
  GC, AT, N = 0, 0, 0

  for line in infile:
  	line = line.strip()
  	if line[0] == ">":
  	  continue
  	else:
  	  for char in line:
  	  	if char == "A" or char == "a" or char == "T" or char == "t":
  	  	  AT += 1
  	  	elif char == "G" or char == "g" or char == "C" or char == "c":
  	  	  GC += 1
  	  	elif char == "N":
  	  	  N += 1
  
  infile.close()

  print("Total bases:", GC+AT+N)
  print("numGC", GC)
  print("numAT", AT)
  print("numN", N)

main()