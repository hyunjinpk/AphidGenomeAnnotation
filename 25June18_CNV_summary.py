# CNV_summary.py

def main():
  infile = open("CNV_candidates_depth_and_SNPs.vcf", "r")
  simple_dict = {}
  for line in infile:
  	col = line.split("\t")
  	if col[0] not in simple_dict:
  	  simple_dict[col[0]] = 0
  	else:
  	  simple_dict[col[0]] += 1

  outstring = ""
  for key in simple_dict:
  	outstring = outstring + key + "\t" + str(simple_dict[key]) + "\n"

  infile.close()
  outfile = open("CNV_summary.txt", "w")
  outfile.write(outstring)
  outfile.close()

main()

# scp ./CNV_summary.py hyunjin@ochmcomp01.ccbb.utexas.edu:/stor/work/Ochman/hyunjin/data/genomes/dovetail