# DNA ToolKit/Code testing file
# Coloring nucleotides
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



from DNAToolKit import *

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'" )
print(f"   {''.join(['|' for c in range(len(DNAStr))])} ")
print(f"3' {reverse_complement(DNAStr)} 5'\n" )

# Output #
# -------------- #
# Sequence: ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA
#[1] + Sequence Length: 61

#[2] + Nucleotide Frequency: {'A': 21, 'C': 12, 'G': 11, 'T': 17}

#[3] + DNA/RNA Transcription: AUUGCUCAUUAGGUACGAUCAAAAAUUCGCUUAAGCCUUAAGGCAAUUUAAACGCGGCUAA

#[4] + DNA String + Reverse Complement:
#5' ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA 3'
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#3' TTAGCCGCGTTTAAATTGCCTTAAGGCTTAAGCGAATTTTTGATCGTACCTAATGAGCAAT 5'

# ------------ #
