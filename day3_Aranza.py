def is_disabled(characters_before_multiplication: str, current_disable: bool = False) -> bool:
    for index in range(len(characters_before_multiplication)-1, 0, -1):
        if characters_before_multiplication[index] != ')':
            continue
        index -= 1
        if characters_before_multiplication[index] != '(':
            continue
        index -= 1
        if characters_before_multiplication[index] != 'o':
            if characters_before_multiplication[index] != 't':
                continue
            index -= 1
            if characters_before_multiplication[index] != "'":
                continue
            if index < 3:
                break
            index -= 1
            if characters_before_multiplication[index] != 'n':
                continue
            index -= 1
            if characters_before_multiplication[index] != 'o':
                continue
            index -= 1
            if characters_before_multiplication[index] != 'd':
                continue
            current_disable = True
            print(characters_before_multiplication)
            print("Disabled")
            break
        index -= 1
        if characters_before_multiplication[index] != 'd':
            continue
        print(characters_before_multiplication)
        print("Enabled")
        current_disable = False
    return current_disable


def find_multiplication(line: str, disabled: bool = False) -> int:
    size_of_string = len(line)
    if(size_of_string == 0):
        return 0
    minimal_size_of_multiplication = len("mul(a,b)")
    if (size_of_string < minimal_size_of_multiplication):
        return 0
    number1 = 0
    number2 = 0
    result = 0
    start_of_mul = -1
    found_multiplication = False

    #   Step 1) Find "mul(" string
    new_index = line.find('mul(')
    new_length = len('mul(')
    if new_index == -1:
        return 0
    start_of_mul = new_index
    new_index = new_index + new_length
    #print("Found MUL")
    #   Step 2) Find number of 1-3 digits
    for number_of_digits in range(3, 0, -1):
        new_length = number_of_digits
        if new_index + new_length > size_of_string:
            continue
        potential_number_str = line[new_index:new_index + number_of_digits]
        if not potential_number_str.isdigit():
            continue
        number1 = int(potential_number_str)
        new_index = new_index + new_length
        #print(f"Found number1:{number1}")
        # Step 3) Find comma
        new_length = 1
        potential_coma_str = line[new_index]
        if potential_coma_str != ',':
            continue
        new_index = new_index + new_length
        #print("Found comma")
        # Step 4) Find number of 1-3 digits
        for number_of_digits in range(3, 0, -1):
            new_length = number_of_digits
            if new_index + new_length > size_of_string:
                continue
            potential_number_str = line[new_index:new_index + new_length]
            if not potential_number_str.isdigit():
                continue
            number2 = int(potential_number_str)
            new_index = new_index + new_length
            #print(f"Found number2:{number2}")
            # Step 5) Find closing parenthesis
            new_length = 1
            potential_parenthesis_str = line[new_index]
            if potential_parenthesis_str != ')':
                continue
            #print(f"Found closing parenthesis")
            result = number1 * number2
            new_index = new_index + new_length
            found_multiplication = True
            #print(f"Index before mul = {start_of_mul}")
            break

    if found_multiplication:
        if (start_of_mul > 0):
            disabled = is_disabled(line[0:start_of_mul-1], disabled)

    if disabled:
        result = 0
    print(f"Result = mul({number1},{number2}) = {result} and DISABLED = {disabled}")
    result += find_multiplication(line[new_index:], disabled)   
    return result

def main():
    result = 0
    with open("input3.txt", "r") as file:
        for line in file:
                result += find_multiplication(line)
    print(result)



if __name__ == "__main__":
    main()