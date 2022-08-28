def compute_dist(l1):
  s1 = list(set(l1))
  d = {}
  for i in s1:
    count = 0
    for j in l1:
      if i == j:
        count += 1
      else:
        continue
    d.update({i : count})
  return d

l1 = list(map(int,input().split()))
d1 = compute_dist(l1)
print(d1)