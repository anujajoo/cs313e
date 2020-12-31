def permute (a, lo, total):
  hi = len(a)
  if (lo == hi):
    if a[1] == 'A':
      total.append(a[:])
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute (a, lo + 1, total)
      a[lo], a[i] = a[i], a[lo]
  return total
      
def sub_sets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    sub_sets (a, b, lo + 1)
    sub_sets (a, c, lo + 1)

def main():
    a = ['A','B','C','D']
    total = []
    permute(a,0, total)
    print(total)
    #a = ['A', 'B', 'C', 'D']
    b = []
    sub_sets (a, b, 0)
    print()
    
main()