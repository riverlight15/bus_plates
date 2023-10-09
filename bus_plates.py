k = int(input())
dictionary = {}

def beginning():
    for i in range(1, k + 1):
        route, other_side = [int(x) for x in input().split()]
        if not route in dictionary:
            dictionary[route] = []
        dictionary[route].append((other_side, i))
    x = [int(x) for x in input().split()]
    check = [(y, []) for y in x[1:]]
    checked = set(x[1:])
    solution(check, checked, dictionary, x)

def solution(check, checked, dictionary, x):
    count = 0
    ans = None
    while len(check) > 0:
        tmp = []
        for given_route, p in check:
            if given_route in dictionary:
                for other_route, index in dictionary[given_route]:
                    if other_route not in checked:
                        exchange = p + [index]
                        if other_route == x[0]:
                            ans = exchange
                            break
                        checked.add(other_route)
                        tmp.append((other_route, exchange))
        check = tmp
        count += 1
        if ans != None:
            break
    if ans == None:
        print('IMPOSSIBLE')
    else:
        print(count)
        for j in ans:
            print(j)


if __name__ == '__main__':
    beginning()