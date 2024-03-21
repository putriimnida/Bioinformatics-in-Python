# DNA Toolkit file

import collections
Nucleotides = ("A", "C", "G", "T")
DNAReverseComplement = {"A": "T", "T": "A", "G": "C", "C": "G"}
DNAStr = "ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA"

# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
#return dict(collections.Counter(seq))

def transcription(seq):
    # DNA -> RNA transcription
    return seq.replace("T", "U")

def reverse_complement(seq):
    # swapping adenine with thymine and guanine with cytosine.
    # reversing newly generated string
    # Pythonic approach. A little faster solution.
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return seq.translate(mapping)[::-1]
    return ''.join([DNAReverseComplement[nuc] for nuc in seq])[::-1]




#Coloring nucleotides
def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        "reset": '\033[0;0m'

    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'



# Reverse Complement
print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'" )
print(f"   {''.join(['|' for c in range(len(DNAStr))])} ")
print(f"3' {reversecomplement(DNAStr)} 5'\n" )