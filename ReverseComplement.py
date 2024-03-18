#DNA reverse complement
# def reverse_complement(seq):
#     return ''.join([DNAReverseComplement[nuc] for nuc in seq])[::-1]

tempStr = "TEST"
DNAStr = "ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA"
print(tempStr[::-1])
print(reverse_complement(DNAStr))

# -- Output -- #
# TSET
# TTAGCCGCGTTTAAATTGCCTTAAGGCTTAAGCGAATTTTTGATCGTACCTAATGAGCAAT
# ------------ #


#DNA reverse complement
print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'" )
print(f"   {''.join(['|' for c in range(len(DNAStr))])} ")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]" )
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n" )

# -- Output -- #
# Sequence: ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA
#
# [1] + Sequence Length: 61
# [2] + Nucleotide Frequency: {'A': 21, 'C': 12, 'G': 11, 'T': 17}
# [3] + DNA/RNA Transcription: AUUGCUCAUUAGGUACGAUCAAAAAUUCGCUUAAGCCUUAAGGCAAUUUAAACGCGGCUAA
# [4] + DNA String + Reverse Complement:
# 5' ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA 3'
#    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# 3' TAACGAGTAATCCATGCTAGTTTTTAAGCGAATTCGGAATTCCGTTAAATTTGCGCCGATT 5' [Complement]
# 5' TTAGCCGCGTTTAAATTGCCTTAAGGCTTAAGCGAATTTTTGATCGTACCTAATGAGCAAT 3' [Rev. Complement]
# ------------ #
