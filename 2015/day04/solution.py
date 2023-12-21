import hashlib

def main():
    input = "bgvyzdsv"
    num = 1
    flag = False
    while True:
        # Adding the current number to the end of the string
        string = input + str(num)
        # Encoding the string with hashlib library
        result = hashlib.md5(string.encode())
        # Check if there is five zeroes
        if result.hexdigest()[0:5] == "00000" and not flag:
            print("Part 1:",string[len(input):])
            flag = True
        # Check if there is six zeroes
        if result.hexdigest()[0:6] == "000000":
            print("Part 2:",string[len(input):])
            break
        num += 1


if __name__ == '__main__':
    main()