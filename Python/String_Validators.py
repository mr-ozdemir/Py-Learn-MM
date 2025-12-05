if __name__ == '__main__':
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False    
    a = input()
    if len(a) > 0 and len(a) < 1000:

      for s in a:
        c = 0
        if s.isalnum():
          alnum = True

        if s.isalpha():
          alpha = True

        if s.isdigit():
          digit = True

        if s.islower():
          lower = True

        if s.isupper():
          upper = True 
      print(alnum)
      print(alpha)
      print(digit)
      print(lower)
      print(upper)
