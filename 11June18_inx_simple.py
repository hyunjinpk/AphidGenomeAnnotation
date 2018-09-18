# inx_simple.py
# See 11June18_Jaquiery.txt for its purpose.

def main():
  infile = open ("./NW1.txt", "r")
  infile2 = open ("./dove_X_nocomment_processed.gff")
  Xlist = infile2.readlines()
  X = ""
  for line in Xlist:
  	X += line

  infile2.close()
  out = ""
  scaffolds = []

  for line in infile:
    new_infile = line.strip()
    new_infile = line.replace('\r', '')
    new_infile = new_infile.strip()
    scaffolds.append(new_infile)
  
  new_scaffolds = []
  for item in scaffolds:
    if item in new_scaffolds:
      continue
    else:
      new_scaffolds.append(item)
  
  numtrue = 0
  numfalse = 0
  for item in new_scaffolds:
    if item in X:
      out = out + item + ",True" + "\n"
      numtrue += 1
    else:
      out = out + item + ",False" + "\n"
      numfalse +=1

  numscaffolds = 9096
  print(numscaffolds, numtrue, numfalse, numtrue + numfalse)

  outfile = open ("TableS1_NCBI_Xonly_simpleout.txt", "w")
  outfile.write(out)
  outfile.close()

main()