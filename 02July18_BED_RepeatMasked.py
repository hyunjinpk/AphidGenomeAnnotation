# 02July18_BED_RepeatMasked.py

def main():
  repeat_masked = "pea_aphid_24Feb2018_fmGlB_custom_repeatmasker.fasta"
  infile = open(repeat_masked, "r")

  scaffold_name = ""
  position = 0
  outstring = ""

  for line in infile:
  	line = line.strip()
  	if len(line) == 0:
  	  continue
  	elif line[0] == ">":
  	  scaffold_name = line[1:]
  	  position = 0
  	else:
  	  if len(line) > 75:
  	  	outstring = outstring + scaffold_name + "\t" + str(position) + "\t" + str(position+100) + "\n"
  	  	position += 100
  	  else:
  	  	position += 100
  infile.close()

  outfile = open("pea_aphid_24Feb2018_fmGlB_RepeatMasked.bed", "w")
  outfile.write(outstring)
  outfile.close()

main()