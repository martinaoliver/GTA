import pandas as pd

ls = []
with open("gene_expression.txt") as in_file:
    lines = in_file.readlines()
    header = lines.pop(0).rstrip().split()
    for line in lines:
        ls.append(line.rstrip().split())
   
dframe = pd.DataFrame(ls, columns=header)

dframe[['Chrom','Start','End','Strand','log2FoldChange','pvalue']] = dframe[['Chrom','Start','End','Strand','log2FoldChange','pvalue']].apply(pd.to_numeric)

bool_index = dframe.pvalue < 0.05
new_dframe = dframe[bool_index]

print (new_dframe[['ID','log2FoldChange','pvalue']])