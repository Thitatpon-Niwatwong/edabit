def dna_to_rna(dna):
    c = []
    sum = {
        'U': 'A',
        'A': 'T',
        'C': 'G',
        'G': 'C'
    }
    a = [x for x in dna]
    for b in a:
        if b in sum.keys():
            c.append(sum[b])
    aJoin = ''.join(c)
    return aJoin


print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))
