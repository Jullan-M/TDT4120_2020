def string_match(dna, segments):
    dna_sequences = []

    n = len(dna)
    for step in range(1, n+1):
        l = n + 1 - step
        for i in range(0, l):
            dna_sequences.append(dna[i:i+step])
    return dna_sequences

print("ACTTACTGG\n" + str(string_match("ACTTACTGG", "")))