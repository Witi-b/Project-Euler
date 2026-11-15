# Burton Number Theory section 1.1 exercise 12
# Find the integer < 1,000,000 that has the longest Collatz sequence
# Usage: python3 14.py n
# Where n is the upper limit number to check
import functools
import sys

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def T(n):
  if n == 1:
    return n
  if n % 2 == 0:
    n = n // 2
    T(n)
  else:
    n = ((3*n) + 1) // 2
    T(n)

def main():
  user_num = int(sys.argv[1])
  highest_sequence = 0
  for i in range(user_num, user_num // 2, -1):
     T.calls = 0
     result = T(i)
     if T.calls > highest_sequence:
        highest_sequence = T.calls
        highest_sequence_num = i
  print(f"The number {highest_sequence_num} has {highest_sequence} sequences")


if __name__ == '__main__':
  main()
