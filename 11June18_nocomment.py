# nocomment.py
# See 11June18_Jaquiery.txt for its purpose.

def main():
  infile = open ("./dove_3_21646.gff", "r")
  lines = infile.readlines()
  out = ""

  for i in range(len(lines)-2):
  	if lines[i][0] != "#":
  	  out += lines[i]
  	elif (lines[i+2][0] != "#"):
  	  out += lines[i]
  	else:
  	  continue

  outfile = open("dove_3_nocomment_processed.gff", "w")
  outfile.write(out)
  outfile.close()

main()