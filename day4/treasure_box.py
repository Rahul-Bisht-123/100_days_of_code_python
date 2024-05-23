'''
- Create a 3*3 2d-array , all filled with empty box
- take two number user prompt for placing the treasure in the 2d-array
'''

treasure = '🍔'
col_name = ["R|C","c1","c2","c3"]

row1 = ["r1 " ,'⬜️' , '⬜️' ,'⬜️']
row2 = ["r2 " ,'⬜️' , '⬜️' ,'⬜️']
row3 = ["r3 " ,'⬜️' , '⬜️' ,'⬜️']


map = f"{col_name} \n{row1} \n{row2} \n{row3}"
print(map)

row_input = input("which row you want to hide the treasure : ")
col_input = input("which column you want to hide the treasure : ")

row_num = int(row_input[1])
col_num = int(col_input[1])

MAP = [row1 , row2 , row3]

MAP[row_num - 1][col_num] = treasure

map = f"{col_name} \n{row1} \n{row2} \n{row3}"
print(map)