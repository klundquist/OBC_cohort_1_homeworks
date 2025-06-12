from Bio.Seq import Seq
from Bio import SeqIO

record = SeqIO.read("test_dna_orf.txt", "fasta")
sequence = record.seq

def find_orfs(sequence):
    orfs_list = []
    for dna_seq in [sequence, sequence.reverse_complement()]:
        for i in range(3):
            last_orf_end = 0
            aa_seq = dna_seq[i:].translate()
            for j in range(len(aa_seq)):
                if aa_seq[j] == 'M' and j > last_orf_end:
                    for k in range(j, len(aa_seq)):
                        if aa_seq[k] == '*':
                            orfs_list.append(aa_seq[j:k+1])
                            last_orf_end = k
                            break
    return orfs_list

orfs = find_orfs(sequence)
print(f"A total of {len(orfs)} ORFs were found.\n")
print(f"The following ORFs were found in the sequence:\n")
for orf in orfs:
    print(orf)

