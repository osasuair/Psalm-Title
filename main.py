import math
import pyautogui


def isint(num: str):
    """

    :param num: The number as a String
    :return: True if the string can be converted to an int, False otherwise
    """
    try:
        num.isnumeric()
        return True
    except AttributeError:
        return False


def binary_search(arr, left: int, right: int, num: int):
    """
    Using recursion, the binary search algorithm is used to search for a number in a list provided by the user

    :param arr: An Array of integers, must be sorted ascending
    :param left: The first index in the list
    :param right: The last index in the list
    :param num: The number being searched for
    :return: True if the number is found in the array, false otherwise
    """
    try:
        if left > right:
            return False
        middle: int = math.floor((left + right) / 2)
        if arr[middle] == num:
            return True
        if num < arr[middle]:
            return binary_search(arr, left, middle - 1, num)
        else:
            return binary_search(arr, middle + 1, right, num)
    except IndexError:
        return False


# Main
def main():
    reader = open("Psalm.txt")
    count = len(reader.readlines())  # Read Number of Lines in txt file
    reader.seek(0)

    # Two Lists that store all the data from the psalm text file
    psalm_num = []
    psalm_title = []

    # Loop splits the psalm text file into the two Lists
    for i in range(count):
        if i % 2 == 0:
            psalm_num.append(int(reader.readline()))
        else:
            psalm_title.append((reader.readline())[:-1])
    reader.close()

    # Loop to verify the user's input is valid and return the psalm that the user request for
    while True:
        user_input = pyautogui.prompt(f'What Psalm Number would you like to see? (1-{len(psalm_num)})', 'Psalm Numbers?'
                                      , '1')

        if user_input is None: break  # break if user selects cancel or exit

        if user_input.isnumeric():
            num = int(user_input)

            if binary_search(psalm_num, 0, len(psalm_num), num):
                pyautogui.alert(text=("Psalm: " + str(user_input) + "\n" + psalm_title[num - 1]), title="Psalm Titles")
                break
            else:
                pyautogui.alert(text="ERROR: That Number does not have a Psalm Title available!\nPlease Try Again!",
                                title="ERROR")
        else:
            pyautogui.alert(text="ERROR: That is not a Number!\nPlease Try Again!", title="ERROR")


if __name__ == '__main__':
    main()
