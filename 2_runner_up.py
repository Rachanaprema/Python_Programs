if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_score= list(set(arr)) 
    unique_score.sort(reverse=True)
    
    if len(unique_score)>1:
        print(unique_score[1])
    else:
        print("no score")
