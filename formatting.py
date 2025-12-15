max_range = 13
max_pie_v = 22/7
# Defining constants at the top


for i in range(1, max_range):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3 ))

print()

for i in range(1, max_range):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3 ))

print()

for i in range(1, max_range):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3 ))

print()

for i in range(1, max_range):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3 ))

print()

for i in range(1, max_range):
    print("No. {0:2} squared is {1:>3} and cubed is {2:>4}".format(i, i ** 2, i ** 3 ))

print()

print("Pi is approximately {0:12}".format( max_pie_v ))
print("Pi is approximately {0:12f}".format( max_pie_v))
print("Pi is approximately {0:12.50f}".format( max_pie_v))
print("Pi is approximately {0:52.50f}".format( max_pie_v))
print("Pi is approximately {0:62.50f}".format( max_pie_v))
print("Pi is approximately {0:72.50f}".format( max_pie_v))

