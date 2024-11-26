length = 21
input = "abcctklpokjp"

a = []

s = []

biggest_string = 0
counter = 0

for i in input:
    i = str(i)
    a.append(i)

for i in range(0, length):
    counter = 0
    for j in range(i+1, length+1):
        if a[j] in s:
            if counter >= biggest_string:
                biggest_string = counter
                print(i, j, biggest_string, s)
                print(f"The biggest string is {s}")
                counter = 0
                s.clear()
                break
            else:
                s.clear()
        else:
            counter += 1
            s.append(a[j])

            if j == length and counter >= biggest_string:
                biggest_string = counter
                counter = 0
                print(f"The biggest string is {s}")
                s.clear()
                
           

print(biggest_string)
