number = int(input("Enter the number :"))


def rows():
    for r in range(1, number + 1):
        for y in range(1, r + 1):
            print(y, end="")
        print(' ')


rows()

num = int(input("Enter number :"))


def sum_num():
    sum1 = 0
    for i in range(1, num + 1):
        sum1 += i
    return sum1


result = sum_num()
print("Sum is :", result)


def print_name():
    name = input("Enter your name: ")
    length = len(name)
    for i in range(length * 2 - 1):
        if i < length:
            character = name[:i + 1]
        else:
            character = name[:length * 2 - i - 1]
        print(character)


print_name()


def reverse():
    word = input("Input a word to reverse: ")
    print(word[::-1])


reverse()


def range_reverse():
    num = int(input("Input a range: "))
    while num >= 1:
        print(num, end=" ")
        num -= 1


range_reverse()
print('\n')


def multiples():
    for i in range(1, 10 + 1):
        print(i * 5, end=" ")


multiples()

print('\n')


def main():
    Limit_number = int(input("Enter the limit number: "))
    Max_display_on_screen = int(input("Enter the maximum outputs to display (Max-display-on-screen): "))
    Target_number = int(input("Enter the target number: "))
    count = 0
    current_number = Target_number

    while current_number <= Limit_number and count < Max_display_on_screen:
        print(current_number, end=" ")
        count += 1
        current_number += Target_number


# With the help of the Internet
if __name__ == "__main__":
    main()
