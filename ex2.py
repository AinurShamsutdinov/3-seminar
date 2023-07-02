input_str: str = input('Enter data: ')
num_int: int = int()
num_float: float = float()
num_float_list: list = input_str.split('.')
text_ans: str
is_upper_case: bool = False
is_float: bool = False

for item in input_str:
    if item.isalpha():
        is_upper_case = item.isupper()
        if is_upper_case:
            break

if len(num_float_list) == 2:
    if (num_float_list[0].count('-', 1) == 0 & num_float_list[0].count('-') <= 1) & num_float_list[1].isnumeric():
        is_float = True

if input_str.isnumeric():
    num_int = int(input_str)
    print(f'Text is integer: {num_int}')
elif is_float:
    num_float = float(input_str)
    print(f'Text is floating poin number {num_float}')
elif is_upper_case:
    print(f'Text lowered case: {input_str.lower()}')
else:
    print(f'Text is lower case: {input_str}')
