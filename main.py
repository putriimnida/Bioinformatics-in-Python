
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






# Function to fetch a sequence from NCBI and print its details
def fetch_sequence(accession_id):
[Entrez.email](http://entrez.email/)
= "
[putrira2112@gmail.com](mailto:putrira2112@gmail.com)
" # Replace with your email
handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text")
sequence_data =
[handle.read](http://handle.read/)
()
print(sequence_data)
# Example usage
accession_id = "NC_000852" # Replace with your accession ID
fetch_sequence(accession_id)



# Translating DNA Sequence
from Bio.Seq import Seq
# Function to translate a DNA sequence into a protein sequence
def translate_dna(dna_sequence):
dna_seq = Seq(dna_sequence)
protein_seq = dna_seq.translate()
print(f"Protein Sequence: {protein_seq}")
# Example usage
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
translate_dna(dna_sequence)



# Function to get the reverse complement of a DNA sequence
def reverse_complement(dna_sequence):
dna_seq = Seq(dna_sequence)
rev_comp_seq = dna_seq.reverse_complement()
print(f"Reverse Complement: {rev_comp_seq}")
# Example usage
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
reverse_complement(dna_sequence)
#Output:
#Reverse Complement: CTATCGGGCACCCTTTCAGCGGCCATTACAATGGCCAT


# Function to parse a GenBank file and print sequence IDs and descriptions
def parse_genbank(file_path):
for record in SeqIO.parse(file_path, "genbank"):
print(f"ID: {[record.id](http://record.id/)}")
print(f"Description: {record.description}\n")
# Example usage
genbank_file = "
[example.gb](http://example.gb/)
" # Replace with your GenBank file path
parse_genbank(genbank_file)
#Output:
#ID: SCU49845 Description: Saccharomyces cerevisiae TCP1-beta gene, partial cds, and Axl2p (AXL2) and Rev7p (REV7) genes, complete cds.



# Function to fetch protein data from UniProt and print details
def fetch_protein(uniprot_id):
handle = ExPASy.get_sprot_raw(uniprot_id)
record = [SwissProt.read](http://swissprot.read/)
(handle)
print(f"ID: {record.entry_name}")
print(f"Description: {record.description}")
print(f"Sequence: {record.sequence}")
# Example usage
uniprot_id = "P12345" # Replace with your UniProt ID
fetch_protein(uniprot_id)
# Output:
# ID: 1433B_HUMAN Description: 14-3-3 protein beta/alpha OS=Homo sapiens OX=9606 GN=YWHAB PE=1 SV=1 
# Sequence: MDFKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRSS...


# Function to calculate the GC content of a DNA sequence
def calculate_gc_content(dna_sequence):
gc_content = GC(dna_sequence)
print(f"GC Content: {gc_content:.2f}%")
# Example usage
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
calculate_gc_content(dna_sequence)
# Output:
# GC Content: 48.78%


# Function to find ORFs in a DNA sequence (NOT YET UNDERSTAND)
def find_orfs(dna_sequence):
dna_seq = Seq(dna_sequence)
orfs = []
for strand, nuc in [(+1, dna_seq), (-1, dna_seq.reverse_complement())]:
for frame in range(3):
length = 3 * ((len(nuc) - frame) // 3) 
# Multiple of three
for pro in nuc[frame:frame + length].translate(to_stop=False):
if len(pro) > 100: 
# Filter ORFs longer than 100 amino acids
orfs.append(pro)
return orfs
# Example usage
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGATGCGT"
orfs = find_orfs(dna_sequence)
for i, orf in enumerate(orfs):
print(f"ORF {i+1}: {orf}")
# Output:
# This will print the ORFs identified in the given DNA sequence.


# Function to perform pairwise sequence alignment (NOT YET UNDERSTAND)
def align_sequences(seq1, seq2):
 alignments = pairwise2.align.globalxx(seq1, seq2)
 for alignment in alignments:
 print(format_alignment(*alignment))
# Example usage
seq1 = "GATTACA"
seq2 = "GCATGCU"
align_sequences(seq1, seq2)
# Output:
# GATTACA || | | GCATGCU Score=4 
# GATTACA | || | GCA-TGCU Score=4 


# Function to perform multiple sequence alignment using ClustalW (NOT YET UNDERSTAND)
def multiple_sequence_alignment(input_file):
clustalw_cline = ClustalwCommandline("clustalw2", infile=input_file)
stdout, stderr = clustalw_cline()
print(stdout)
# Example usage
input_file = "sequences.fasta" # Replace with your input file path
multiple_sequence_alignment(input_file)
# Output: 
# The ClustalW output will display the multiple sequence alignment results in the terminal

