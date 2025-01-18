
def split_and_join(line):
    # write your code here
    word = line.split(" ")
    return "-".join(word)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
