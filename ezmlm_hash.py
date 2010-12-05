def ezmlm_hash(addr):
  h = 5381
  for c in addr:
    h = ((h + (h << 5)) ^ ord(c)) % (2 << 31)
  h = h % 53
  return h