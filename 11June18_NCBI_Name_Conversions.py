# NCBI_Name_Conversions.py
# See 11June18_Jaquiery.txt for its purpose.

def dictionary_maker():
  infile = open("./dict.txt", "r")
  my_dict = {}

  for line in infile:
  	line = line.strip()
  	if ("GL" in line):
  	  key = line[:8]
  	  val = line[11:]
  	  my_dict[key] = val

  infile.close()
  return my_dict

def main():
  # Dictionary maker: Reads NCBI_name_conversion.txt and generates a dictionary for GL* vs. NCBI namings.
  my_dict = dictionary_maker()
  
  out = ""
  infile = open("./TableS1_Xonly.txt")

  for line in infile:
  	line = line.strip()
  	line = line + "," + my_dict[line[:8]] + "\n"
  	out += line

  outfile = open("TableS1_Xonly_NCBI.txt", "w")
  outfile.write(out)
  outfile.close()

main()
