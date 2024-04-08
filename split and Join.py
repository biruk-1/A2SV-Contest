def split_and_join(line):
    # write your code here
    myStr = ''
    for letters in line:
        if letters == " ":
            myStr+= '-'
        else:
            myStr+=letters
    return myStr

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
