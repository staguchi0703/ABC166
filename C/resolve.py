def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]

    H_list = [int(item) for item in input().split()]

    path_list = [[int(item) for item in input().split()] for _ in range(M)]

    path_list2 = [[] for _ in range(N+1)]

    for A, B in path_list:
        path_list2[A] += [B]
        path_list2[B] += [A]

    temp_list = []
    for item in path_list2:
        temp_list.append(list(set(item)))
    
    path_list2 = temp_list

    # print(path_list2)

    def nice(i):
        if len(path_list2[i]) >= 1:
            for j in path_list2[i]:
                if H_list[i-1] <= H_list[j-1]:
                    return False
            else:
                return True
                
        else:
            return True


    cnt = 0
    for i in range(N):
        if nice(i+1):
            cnt += 1
            # print(i+1)
    
    print(cnt)


if __name__ == "__main__":
    resolve()
