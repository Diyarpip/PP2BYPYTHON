s = input()

word_to_digit = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}

digit_to_word = {
    "0": "ZER",
    "1": "ONE",
    "2": "TWO",
    "3": "THR",
    "4": "FOU",
    "5": "FIV",
    "6": "SIX",
    "7": "SEV",
    "8": "EIG",
    "9": "NIN"
}


for op in "+-*":
    if op in s:
        left, right = s.split(op)
        operation = op
        break


def words_to_number(text):
    num = ""
    for i in range(0, len(text), 3):
        triplet = text[i:i+3]
        num += word_to_digit[triplet]
    return int(num)

a = words_to_number(left)
b = words_to_number(right)


if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
else:
    result = a * b


result_str = str(result)
answer = ""

for digit in result_str:
    answer += digit_to_word[digit]

print(answer)
