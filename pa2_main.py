if __name__ == "__main__":
    cap_join = "calvin and hobbes are the first spacemen on mars"
    str = cap_join.split()
    s = ""
    for index in range(len(str)):
        s += str[index].capitalize()
        s += " "

    print(s)





