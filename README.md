# AI-CNF
Write a program that will read a Knowledge Base (KB) that will consists of many sentences formatted in the CNF format, and a query (one sentence) also in the CNF format from a text file. You should ask the user to enter the name of the file at the beginning of your program and then you should read that file and print its content on the screen. Then your code should try to entail the query from the KB and outputs whether it can be entailed or not.

The format of the input file will be having the KB on a line and the query on the next line. The file may contain more than one request and it will be listed as :

( A v  ~B) ^ ( C v B) ^ ( ~C)
A

( A v  B) ^ ( C v ~B) ^ ( D v ~C)
A ^ B 


Output should be :
KB:   ( A v  ~B) ^ ( C v B) ^ ( ~C)
query:   A

KB:  ( A v  B) ^ ( C v ~B) ^ ( D v ~C)
query:  A ^ B 

Yes, A can be entailed.

No, A ^ B can’t be entailed.
