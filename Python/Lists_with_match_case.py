if __name__ == '__main__':
    n = int(input())
    mylist = []
    
    for _ in range(n):
        parts = input().split()
        operation = parts[0]

        match operation:
            case "insert":
                index = int(parts[1])
                value = int(parts[2])
                mylist.insert(index, value)
            case "print":
                print(mylist)
            case "remove":
                value = int(parts[1])
                mylist.remove(value)
            case "append":
                value = int(parts[1])
                mylist.append(value)
            case "sort":
                mylist.sort()
            case "pop":
                mylist.pop()
            case "reverse":
                mylist.reverse()
            case _:
                exit()
