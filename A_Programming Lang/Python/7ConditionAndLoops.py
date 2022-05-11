# Condtion statement used to check conditions satisfied or not
a = 1000
b = 100

# Smiple if
if a > b:
    print("Yes a is bigger than b")

# if..else
if a < b:
    print("No b is bigger than a")
else:
    print("no a is bigger than b")

# if..elif..else
if a == b:
    print("Both equals")
elif a < b:
    print("No b is bigger than")
else:
    print("no a is bigger than b")

# Nesetd if..else
if a != b:
    if a < b:
        print("no b is bigger than a")
    else:
        print("no a is bigger than b")
else:
    print("both equals")

# Short if..else
print("A") if a > b else print("B")



# Loops :-

# While loop :-
i = 1
while i < 10:
    i = i + 1
    if i == 8:
        break
    if i == 5:
        continue
    print(i)
else:
    print("If condition not satisfied come here or after loop completes")

# For Loop :-
for x in range(0, 10):  # Any iterable
    print(x)
print("Finished")

for q in range(10, 14, 2):
    for e in range(20, 25):
        print(q, e)