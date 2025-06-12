conda create -n hw2 python=3.10
conda activate hw2
pip install pandas seaborn matplotlib biopython
python analyze_eukaryotes.py > euk_stats.txt
python find_orfs.py > orf_results.txt
