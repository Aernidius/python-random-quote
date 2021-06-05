import random
def hehhh():
  print("Keep it logically awful.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  hehhh()

