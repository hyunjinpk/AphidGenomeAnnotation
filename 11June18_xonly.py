# xonly
# See 11June18_Jaquiery.txt for its purpose.

def main():
  infile = open ("./TableS1_NCBI.txt", "r")
  out = ""
  for line in infile:
    if ",X," in line:
      out += line
  infile.close()
  
  outfile = open ("TableS1_NCBI_Xonly.txt", "w")
  outfile.write(out)
  outfile.close()

main()