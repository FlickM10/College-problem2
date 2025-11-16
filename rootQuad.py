a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))

r1 = ( -b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
r2 = ( -b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)

print(f" One root is r1 = {r1:0.4} ")
print(f" Another root is r2 = {r2:0.4} ")

