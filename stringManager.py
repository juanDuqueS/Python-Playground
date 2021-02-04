def invertString(word):
  if len(word) == 0:
    return word
  else:
    return invertString(word[1:]) + word[0]