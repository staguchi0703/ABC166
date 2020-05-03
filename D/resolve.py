def resolve():
    '''
    code here
    '''
    X = int(input())

    max_num = int(2 * (10 ** 9) ** (1/5))

    is_flag = False
    for i in range(-1*max_num, max_num):
        for j in range(-1*max_num, max_num):
            if i ** 5 - j ** 5 == X:
                print(i, j)
                is_flag = True
                break
        
        if is_flag:
            break





if __name__ == "__main__":
    resolve()
