def count_substring(string, sub_string):
  count = 0
  i = 0
  a = len(sub_string)

  while(i < len(string)):
    sstring = string[i:i+a]
    if sstring == sub_string: 
      count = count + 1
    i = i + 1
  return count
