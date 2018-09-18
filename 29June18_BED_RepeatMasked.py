# 29June18_BED_RepeatMasked.py
# creates BED file for the non-repeat region

def main():
  assembly = "pea_aphid_24Feb2018_fmGlB.fasta"
  infile = open(assembly, "r")

  scaffold_name = ""
  base_position = 0
  outstring = ""
  bases = ["A", "T", "C", "G"]
  
  no_end_of_line = ""
  for line in infile:
  	if line[0] == ">":
  	  no_end_of_line = no_end_of_line + "\n" + line
  	else:
  	  line = line.strip()
  	  no_end_of_line += line

  for line in no_end_of_line:
  	if line[0] == ">":
  	  line = line.strip()
  	  scaffold_name = line[1:]
  	  base_position = 0
  	  was_in_base = False
  	else:
  	  for char in line:
  	  	if char in bases:
  	  	  is_in_base = True
  	  	  if (was_in_base != is_in_base):
  	  	    outstring = outstring + scaffold_name + "\t" + str(base_position)
  	  	  base_position += 1
  	  	  was_in_base = True
  	  	else:
  	  	  is_in_base = False
  	  	  if (was_in_base != is_in_base):
  	  	    outstring = outstring + "\t" + str(base_position-1) + "\n"
  	  	  base_position += 1
  	  	  was_in_base = False

  outfile = open("pea_aphid_24Feb2018_fmGlB_RepeatMasked.bed", "w")
  outfile.write(outstring)
  outfile.close()

main()
