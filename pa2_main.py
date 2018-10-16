def cap_join(string_list):
    word = cap_join
    word = ' '.join(s[1].upper() + s[1:] for s in string_list)


if __name__ == "__main__":
    cap_join = "calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"
    print(cap_join)
