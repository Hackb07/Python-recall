# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("Enter a principle: "))
    if principle <= 0:
        print("principle must be greater than zero")

while rate <= 0 :
    rate = float(input("Enter a Rate: "))
    if rate <= 0:
        print("Rate must be greater than zero")

while time <= 0 :
    time = int(input("Enter a Time(in Years): "))
    if time <= 0:
        print("Time must be greater than zero")

print(f"The Principle : {principle}\n"
      f"The Rate of Interest :{rate}\n"
      f"The Time Duration is : {time}")

total = principle * pow((1+ rate /100),time)
print(f"The Balance after {time} years/s : ${total:.2f}")