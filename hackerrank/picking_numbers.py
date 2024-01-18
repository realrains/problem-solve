def pickingNumbers(a):
    cnt = [0 for _ in range(100)]
    tmp = [0 for _ in range(100)]
    for i in a:
        cnt[i] += 1
    
    for i in range(1, 100):
        tmp[i] = cnt[i] + cnt[i-1]
    
    return max(tmp)
