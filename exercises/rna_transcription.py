rna_dict = {'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U',
            '': ''}


def to_rna(dna_strand):
    rna_strand = [rna_dict[i] for i in dna_strand]
    return ''.join(rna_strand)


print(to_rna("ACGTGGTCTTAA"))
