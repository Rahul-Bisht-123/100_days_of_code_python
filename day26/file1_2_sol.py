with open("file1.txt") as file1:
  list1 = [line.strip() for line in file1]
  print(list1)

with open("file2.txt") as file2:
  list2 = [line.strip() for line in file2]
  print(list2)

ans_list = [int(l1) for l1 in list1 if l1 in list2]
print(ans_list)