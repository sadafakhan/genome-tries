# genome-tries
```genome-tries``` takes a directory of genome-files as input and finds target DNA sequences using a prefix trie. The input files are quite large, resulting in a longer runtime of about 20 minutes. 

Args: 
* ```targets```: text file with target DNA sequences
* ```genomepath```: a directory of genome-files

Returns: 
* ```output.txt```: text file listing out matches between targets and genome files

To run: 
```
src/run.sh input/targets input/hg19-GRCh37
```

PROJECT 4 OF LING473 (08/27/2021)
