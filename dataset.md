# Data set
As test data we used genomic sequences from the genomes of human, mouse, crab eating macaque and naked mole rat. Assembly versions were selected to have the possibility for both Ensembl orthology prediction and UCSC 100-way alignmnent to be exploited (for future validation over the same benchmark). Corresponding fasta were downloaded from UCSC repository, in their softmasked version:

Homo sapiens (hg38 GCA_000001405)
Mus musculus (mm10 GCA_000001635)
Heterocephalus glaber (hetGla2 GCA_000247695)
Macaca fascicularis (macFas5 GCA_000364345)

respect to Ensembl they differ only for the number of patches so far applied as notified by the presence of a different final patch version number (here not reported), but patches do not alter coordinates so that they can be safely disregarded. 

Note that we use only the human and mouse genomes and their pairwise alignment for evaluation. The other genomes are merely there for some of the methods to help in identifying seeds for a human-mouse alignment.


>*Mario'original notes*

>we identified pairs of orthologous genes in human and mouse (which DB?) and added the closest homolog in rat and cow, if such a homolog exists. For each such gene family we cut out the region of the genome between start and stop codon and included a flanking region of 5000bp. The MULTIZ alignment constructed by the UCSC Genome Browser team served as a gold standard for evaluating the seeds. This multiple sequence alignment was projected to a pairwise alignment of the human and mouse genome only.


Orhologs have been queried from Biomart (the Ensembl interface to access homology prediction) for each pair of species out of the four previously mentioned. Ortholog pairs have been added to a graph from which only complete 4-tuples have been extracted that had maximal score. By means of complete tuple it is intended that each organism in the tuple is in some homology relation to all other organisms within the same tuple. The score is the one reported by Ensembl as 0 or 1, respectively representing low and high confidence in the orthology relation. Such a score is obtained by thresholding the sum of two components: WGA, based on the alignment of putative homologous regions and GOC, according to which genes lying inbetween genes which have been in turn identified as homologous are rewarded.  
The only orthology type allowed was one2one to avoid multiple homology relations. 


After retrieving the gff for prediction over the four genomes, in order to avoid any bias towards those genes which include a larger number of transcripts, a principal transcript has been picked for each gene. On average, for human and mouse we found respectively 3.5 and 2.3 alternative transcripts per gene. By definition, in Ensembl a gene is the collection of transcripts (obtained upon aligning mRNA and proteins from UniProtKB and RefSeq) whose coding regions somehow overlap. 

To this end, for each gene, either from human or mouse, which has been included in some orthology tuple as previously explained and for each transcript in that gene, all information available in Ensembl has been collected (based on Appris, TSL, GeneCode basic) and the transcript ranking the highest has been selected.



