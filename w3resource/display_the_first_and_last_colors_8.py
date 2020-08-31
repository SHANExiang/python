# Write a Python program to display the first and last colors from the
# following list.
# color_list = ["Red","Green","White" ,"Black"]



def display_the_first_and_last_colors_from_list(lis):
    return "%s %s" % (lis[0], lis[-1])


if __name__ == '__main__':
    lis = ["Red","Green","White" ,"Black"]
    print(display_the_first_and_last_colors_from_list(lis))
