import random


with open("..\challenges.txt", "r") as file:
    line = file.readline()
    #print(line)
    my_str = ''
    challenge_list = []
    while line != '':
        phrase_list = line.replace("\\n", "\n")
        for i in phrase_list:
            my_str += i
        line = file.readline()
    print(my_str)
    # challenge_list.append(my_str)
    # print(challenge_list)

# for i in range(24):
#
#
# def main():
#     print("hello world")
#
# main()
