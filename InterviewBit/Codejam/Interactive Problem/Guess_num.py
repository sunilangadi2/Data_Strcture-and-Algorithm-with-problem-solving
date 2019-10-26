'''Problem
This problem is a well-known classic; we present it primarily 
as an opportunity for you to try out the interactive judging system.

We are thinking of an integer P within the range 
(A,B] — that is, A < P ≤ B. You have N tries to guess our number. 
After each guess that is not correct, we will tell you whether 
P is higher or lower than your guess.

Input and output
This problem is interactive, which means that the concepts of 
input and output are different than in standard Code Jam problems. 
You will interact with a separate process that both provides you 
with information and evaluates your responses. All information comes 
into your program via standard input; anything that you need to 
communicate should be sent via standard output. 
Remember that many programming languages buffer the output by default, 
so make sure your output actually goes out 
(for instance, by flushing the buffer) before blocking to wait 
for a response. See the FAQ for an explanation of what 
it means to flush the buffer. Anything your program sends through 
standard error is ignored, but it might consume some memory and be 
counted against your memory limit, so do not overflow it. 
To help you debug, a local testing tool script (in Python) is 
provided at the very end of the problem statement.

Initially, your program should read a single line containing a 
single integer T indicating the number of test cases. 
Then, you need to process T test cases.

For each test case, your program will read a single line with two integers 
A and B, representing the exclusive lower bound and inclusive upper bound, 
as described above. In the next line, you will read a single integer N, 
representing the maximum number of guesses you can make. 
Your program will process up to N exchanges with our judge.

For each exchange, your program needs to use standard 
output to send a single line with one integer
 Q: your guess. In response to your guess, 
 the judge will print a single line with one word to your input stream, 
 which your program must read through standard input. 
 The word will be CORRECT if your guess is correct, 
 TOO_SMALL if your guess is less than the correct answer, 
 and TOO_BIG if your guess is greater than the correct answer.
  Then, you can start another exchange.

'''



import sys

def solve(a, b):
  m = (a + b) // 2
  print(m)
  sys.stdout.flush()
  s = input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  else:
    b = m - 1
  solve(a, b)

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  _ = int(input())
  solve(a + 1, b)
