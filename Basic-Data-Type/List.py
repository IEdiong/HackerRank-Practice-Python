if __name__ == '__main__':
    n = int(input())
    lst = []
    cmd = []
    cmd_para = []

    for _ in range(n):
        c, *para = input().split()
        cmd.append(c)
        cmd_para.append([int(str) for str in para])

    # print(cmd, cmd_para)

    for k, v in zip(cmd, cmd_para):
        if k == 'insert':
            lst.insert(v[0],v[1])
        elif k == 'print':
            print(lst)
        elif k == 'remove':
            lst.remove(v[0])
        elif k == 'append':
            lst.append(v[0])
        elif k == 'sort':
            lst.sort()
        elif k == 'pop':
            lst.pop()
        elif k == 'reverse':
            lst.reverse()
        elif k == 'extend':
            lst.extend(v)
        elif k == 'index':
            print(lst.index(v[0]))
        elif k == 'count':
            print(lst.count(v[0]))

    # print(lst)
