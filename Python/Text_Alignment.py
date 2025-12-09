if __name__ == '__main__':
  a = "H"
  n = int(input())
  if (n > 0) and (n < 50) and (n % 2 == 1):
    for i in range(n):
      print(a.center(n * 2,' '))
      a = a + "HH"
    
    for j in range(n + 1):
      print(("H" * n).center((n * 2),' '),end ="")
      print(("H" * n).center((n * 6) ,' '))

    for k in range((n + 1) // 2):
      print(("H" * n * 5).center((n * 6) ,' '))

    for j in range(n + 1):
      print(("H" * n).center((n * 2),' '),end ="")
      print(("H" * n).center((n * 6) ,' '))

    f = (n * 2) - 1
    for z in range(n):
      print(("H" * f).center((n * 10),' '))
      f = f - 2
