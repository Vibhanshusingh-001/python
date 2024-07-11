from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Create a DNA sequence
dna_sequence = Seq("ATCGATCGATCG" )  # No need to specify the alphabet

# Create a SeqRecord with the DNA sequence
seq_record = SeqRecord(dna_sequence, id="example_id", description="Example DNA sequence")

# Print the SeqRecord
print(seq_record)


