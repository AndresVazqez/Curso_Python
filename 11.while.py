## Continous loops

for char in "python":
    if char == "h":
        continue
    print(char)

print("----------------------")

text="This is a simple text!"
count = 0
for char in text:
    if char == " ":
       continue 
    count += 1

print(count)

print("--------------------------")

email = input("enter your email \n")
valid=False
for char in email:
    if char == '@':
        valid=True
        break

else:
    valid = False

print(valid)