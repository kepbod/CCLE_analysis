## 1. Download the gene expression file (e.g. `CCLE_RNAseq_genes_rpkm_20180929.gct`) from [CCLE](https://portals.broadinstitute.org/ccle/data).
## 2. Classify samples into the highest quarter group (labeled as **0** in `exp_group.txt`) and the lowest quarter group (labeled as **1** in `exp_group.txt`) according to expression levels of one specific gene.
```
./group.py checked_gene gene_list.txt CCLE_RNAseq_genes_rpkm_20180929.gct > exp_group.txt
```
* input:
  * checked_gene: gene symbol used to classify groups (e.g. LIG3)
  * gene_list.txt: list of tested genes 
  * CCLE_RNAseq_genes_rpkm_20180929.gct: gene expression file
* output:
  * exp_group.txt: gene_symbol group_label expression_level
## 3. Plot boxplots
```
./plot.R exp_group.txt boxplots.pdf
```