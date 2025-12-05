if __name__ == '__main__':

  di = {}
  n=int(input())

  if n >= 2 and n <= 10:
    for _ in range(n):
      al = input()
      name_parts = al.split()
      isim = name_parts[0]
      score_strings = name_parts[1:]
      scores = [float(s) for s in score_strings]


      for n in scores:
        if not (0 <= n <= 100):
            exit()

      di[isim] = scores

    ar = input()

    if ar in di:
      target_scores = di[ar]
      total_score = 0
      for i in target_scores:
        total_score = total_score + i

      print(f"{total_score / len(target_scores):.2f}")
