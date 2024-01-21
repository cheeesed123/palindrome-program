def isPalindrome(x) -> bool:
    len_of_num = len(x) - 1
    list_of_num = []
    for i in x:
        list_of_num.append(i)
    x = 0
    y = len_of_num
    while True:
        if list_of_num[x] == list_of_num[y]:
            x += 1
            y -= 1
        else:
            return False
        if x >= y:
            return True

def main():
    palindrome_num = input("Please input a palindrome:")

    if isPalindrome(palindrome_num):
        print("Is palindrome")
    else:
        print("Is not a palindrome")

    # run again screen
    print("Want to try another palindrome? (Y or N)")
    answer = input().strip().lower()
    if answer in ["y", "yes"]:
        main()
    else:
	print("Bye!")
        exit
main()
