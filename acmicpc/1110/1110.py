n = int(input())

check = n
new_number = 0
temp = 0
count = 0

while True:
    count += 1
    temp = n // 10 + n % 10
    new_number = (n % 10) * 10 + temp % 10
    n = new_number
    if new_number == check:
        break

print(count)
