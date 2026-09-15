# nested_loop =  A loop within another Loop (outer,inner)
#                   outer_loop :
#                       inner_loop:

n = int(input("Enter Length :"))
m = int(input("Enter Breadth : "))
symbol = input("Enter Symbol : ")
for x in range(n):
    for y in range(m):
        print(symbol,end ="" )

    print()