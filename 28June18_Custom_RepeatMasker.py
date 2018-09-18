# 28June18_Custom_RepeatMasker.py

def main():
  assembly = "pea_aphid_24Feb2018_fmGlB.fasta"
  infile = open(assembly, "r")
  
  outstring = ""
  for line in infile:
  	if line[0] == ">":
  	  outstring += line
  	else:
  	  for char in line:
  	  	if char=="A" or char=="T" or char=="C" or char=="G" or char=="\n":
  	  	  outstring += char
  	  	elif char=="N" or char=="a" or char=="t" or char=="c" or char=="g":
  	  	  continue
  
  infile.close()

  outfile = open("pea_aphid_24Feb2018_fmGlB_custom_repeatmasker.fasta", "w")
  outfile.write(outstring)
  outfile.close()

main()