#!/usr/bin/env python2.7

flag = "REDACTED"

def main():
  try:
    seed = int(raw_input("Give me a good seed:\n"))
  except ValueError:
    print("integers only please")
    exit(1)
  a=252149039917
  b=13 #careful seed cracking regulars
  m=2**48
  res=[]
  for _ in range(761):
      seed = (a*seed + b) % m
  for i in range(12):
      seed = (a*seed + b) % m
      if (seed < 253327472328704):
          print("Failed on round",i)
          exit(1)
  print("well done")
  print(flag)
  exit(0)
if __name__ == "__main__":
    main()
