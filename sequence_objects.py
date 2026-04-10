# Sequences act like strings
### in most ways, we can deal with Seq objects as if they were normal Python strings, for example getting the length, or iterating over the elements:
>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCG")
>>> for index, letter in enumerate(my_seq):
  print("%i %s" % (index, letter))
  print(len(my_seq))
  
