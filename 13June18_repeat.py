# repeat.py
# See 12June18_assemblystats.txt

def main():
  infile = open("./dove_scatters.fasta", "r")

  lower_cases = 0
  for line in infile:
  	if line[0] == ">":
  	  continue
  	else:
  	  for char in line:
  	  	if char.islower():
  	  	  lower_cases += 1

  infile.close()
  print("# of lower cases in unassembled scaffolds:", lower_cases)

main()
