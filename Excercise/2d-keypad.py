row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
row4 = ["#",0,"*"]

numpad = [row1,row2,row3,row4]
for row in numpad:
    for numbers in row:
        print(numbers,end=" ")
    print()