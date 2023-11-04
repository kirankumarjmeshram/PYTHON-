def myfunc(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            result += input_string[i].lower()
        else:
            result += input_string[i].upper()
    return result

print(myfunc('Anthropomorphism')) #aNtHrOpOmOrPhIsM