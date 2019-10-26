T=int(input())

for t in range(T):
  n, m = map(int, input().split())
  res = []
  empty = 0
  for _ in range(n):
    row = input().strip()
    
    if row == '?'*m:
      empty += 1
    else:
      newrow = ''
      let = next(c for c in row if c != '?')
      
      for c in row:
        if c != '?':
            let=c
        else:
            let=let
            
        newrow += let       
      res += [newrow] * (empty+1)
      empty = 0
  res += [res[-1]] * (n - len(res))
  print('Case #%d:' % (t+1))
  print('\n'.join(res))
