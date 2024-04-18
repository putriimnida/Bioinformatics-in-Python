
# DNA ToolKit/Code testing file
from DNAToolKit import *


rndDNAStr = "ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA"

print(validateSeq(rndDNAStr))

# -- Output -- #
# ATTGCTCATTAGGTACGATC
# ------------ #


# DNA ToolKit/Code testing file
from DNAToolKit import *

rndDNAStr2 = "ATTCGCTGAGGCCCccTaTTTAACGTAA"
print(validateSeq(rndDNAStr2))

# -- Output -- #
# ATTCGCTGAGGCCCCCTATTTAACGTAA
# ------------ #


# DNA ToolKit/Code testing file
from DNAToolKit import *

rndDNAStr3 = "ATTCGCTGAGGXCCccTaTTTAACGTAAX"
print(validateSeq(rndDNAStr3))

# -- Output -- #
# False
# ------------ #


# DNA Toolset/Code testing file
from DNAToolKit import *
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)for nuc in range(20)])

print(validateSeq(rndDNAStr))

# -- Output -- #
# ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA
# ------------ #

# Counting a random DNA sequence for testing:
print(countNucFrequency(randDNAStr))

# -- Output -- #
# {'A': 3, 'C': 7, 'G': 4, 'T': 6}
# ------------ #


# DNA Toolkit
# def transcription(seq):
    # DNA -> RNA transcription
    # return seq.replace("T", "U")

# DNA transcription
from DNAToolKit import *

DNAStr = "ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA"
print(transcription(DNAStr))

# -- Output -- #
# AUUGCUCAUUAGGUACGAUCAAAAAUUCGCUUAAGCCUUAAGGCAAUUUAAACGCGGCUAA
# ------------ #


tempStr = "TEST"
print(tempStr[::-1])
print(reverse_complement(DNAStr))

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'" )
print(f"   {''.join(['|' for c in range(len(DNAStr))])} ")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]" )
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n" )



print(f'[5] + GC Content: {gc_content(DNAStr)}%\n' )

print(
    f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')


# DNA Toolset/Code testing file

from bio_seq import bio_seq
from utilities import read_FASTA, readTextFile, writeTextFile

test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "RNA")

print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.reverse_complement())
print(test_dna.gc_content())
print(test_dna.gc_content_subsec())
print(test_dna.translate_seq())
print(test_dna.codon_usage('L'))

for rf in test_dna.gen_reading_frames():
    print(rf)


print(test_dna.all_proteins_from_orfs())



