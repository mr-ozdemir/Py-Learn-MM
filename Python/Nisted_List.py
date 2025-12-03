if __name__ == '__main__':

  all_list = []
  n = int(input())
  if n >= 2 and n <=5:

    for _ in range(n):
      name = input()
      score = float(input())
      all_list.append([name, score])

    unique_list = sorted(list(set(score for name, score in all_list)))
    value= unique_list[1]
    names  = [
        name for name, score in all_list
        if score == value ]
    
    sorted_names=sorted(names)

    for i in sorted_names:
      print(i)

                    
                    
      
