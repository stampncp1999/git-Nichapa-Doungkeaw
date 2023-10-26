def find_max(data):
    candidate = None
    count = 0

    for num in data:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate

n = int(input("Please enter the number of data points: "))

data_input = input("Enter data points separated by a delimiter: ")
data = []
current_num = ""
for char in data_input:
    if char.isdigit():
        current_num += char
    elif current_num:
        data.append(int(current_num))
        current_num = ""


majority_element = find_max(data)

if data.count(majority_element) >= n // 2:
    print(f"The majority element is {majority_element}")
else:
    print("There is no majority element in this dataset.")