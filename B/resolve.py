def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    
    data = [input() for _ in range(2*K)]

    sunuke = [0 for _ in range(N)]

    for i in range(K):
        d = data[i*2]
        okashi = data[i*2 + 1].split()
        for j in okashi:
            sunuke[int(j)-1] += 1


    cnt = 0
    for k in sunuke:
        if k == 0:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()
