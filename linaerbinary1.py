customerids = [101, 102, 103, 104, 105]

searchid = int(input("Enter Customer Account ID: "))

found = False
for i in customerids:
    if i == searchid:
        found = True
        break

if found:
    print("Linear Search: Customer Account ID Found")
else:
    print("Linear Search: Customer Account ID Not Found")

low = 0
high = len(customerids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if customerids[mid] == searchid:
        found = True
        break
    elif searchid > customerids[mid]:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Binary Search: Customer Account ID Found")
else:
    print("Binary Search: Customer Account ID Not Found")