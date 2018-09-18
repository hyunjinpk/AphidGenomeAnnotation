# ina_simple.py
# See 11June18_Jaquiery.txt for its purpose.

def main():
  infile = open ("./TableS1_NCBI_Xonly.txt", "r")
  infile_chr1 = open ("./dove_1_nocomment_processed.gff")
  infile_chr2 = open ("./dove_2_nocomment_processed.gff")
  infile_chr3 = open ("./dove_3_nocomment_processed.gff")
  list_chr1 = infile_chr1.readlines()
  list_chr2 = infile_chr2.readlines()
  list_chr3 = infile_chr3.readlines()
  Alist = list_chr1 + list_chr2 + list_chr3
  A = ""
  for line in Alist:
  	A += line

  infile_chr1.close()
  infile_chr2.close()
  infile_chr3.close()
  out = ""
  scaffolds = []

  for line in infile:
    new_infile = line.strip()
    new_infile = line.replace('\r', '\n')
    new_infile = new_infile.split()

  new_scaffolds = []
  for item in new_infile:
    if item in new_scaffolds:
      continue
    else:
      new_scaffolds.append(item)
  print(new_scaffolds)
  
  numtrue = 0
  numfalse = 0
  for item in new_scaffolds:
    if item in A:
      out = out + item + ",True" + "\n"
      numtrue += 1
    else:
      out = out + item + ",False" + "\n"
      numfalse += 1

  numscaffolds = numtrue + numfalse
  print(numscaffolds, numtrue, numfalse)

  outfile = open ("TableS1_NCBI_Xonly_againstA.txt", "w")
  outfile.write(out)
  outfile.close()

main()