def char_count(str):
  result = []
  i = 0

  while i < len(str)-1:
    char = str[i]
    print(i, char, result)
    if result[i][0] == char:
      result[i][1] += 1
    else:
      result[i] = [char, 1]
    i += 1
  return result

char_count("apple")