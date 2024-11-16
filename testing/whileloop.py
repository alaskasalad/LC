# format:
# while (test expression):
    # do this;
    # increment value -> no infinte loop

# OR

# while (test expression):
    # do this
    # if (condition):
        # break;
    # increment test expression


number = 1;
while (number <= 100):
    print(number)
    number += 5

var = 1;
for i in range (4):
    for j in range (4):
        print(i, j)
 
s = "code"
for i in s:
    print(i)
