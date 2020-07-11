import time as t
second = int(input("How many second to wait :"))

for i in range(second):
    print(str(second-i)+ " seconds remaining ")
    t.sleep(1)

print("Time Up")
