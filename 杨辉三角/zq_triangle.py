from copy import deepcopy

def fun(m):
    if m == 1:
        return [1, 1]
    arr = [1]
    mid = m // 2
    for i in range(1, mid + 1):
        n = get_n_by_recursion(m, i)
        arr.append(n)
    if m % 2 == 0:
        tmp = deepcopy(arr[:mid])
    else:
        tmp = deepcopy(arr[:mid+1])
    print(len(tmp))
    tmp.reverse()
    arr.extend(tmp)
    return arr

def get_n_by_recursion(m, i):
    if i == 0 or m == i:
        return 1
    if m == 2 and i == 1:
        return 2
    return get_n_by_recursion(m-1, i-1) + get_n_by_recursion(m-1, i)


from copy import deepcopy
def get_n(m):
    arr = [1, 1]
    for j in range(2, m+1):
        new_arr = [1]
        mid = j // 2
        for i in range(1, mid+1):   
            n = arr[i-1] + arr[i]   
            new_arr.append(n)

        arr = deepcopy(new_arr)
        if j % 2 == 0:
            tmp = deepcopy(arr[:mid])
        else:
            tmp = deepcopy(arr[:mid+1])
        
        tmp.reverse()
        arr.extend(tmp)
        
    return arr



def main():
    print("input m :")
    m = int(input())
    # print(fun(m))
    print(get_n(m))



if __name__ == '__main__':
    main()