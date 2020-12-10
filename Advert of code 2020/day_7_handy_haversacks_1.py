from pprint import pprint

r = 0
bags = {}

while 1:
    line = input()
    if not line:
        break
    main_bag, right = line.split(' contain ')
    main_bag = main_bag.replace('bags', 'bag')
    right = right.replace('.', '').replace('bags', 'bag')

    small_bags = right.split(', ')
    bags_with_num = {}
    for bag in small_bags:
        num, bag_name = bag.split(' ', 1)
        try:
            bags_with_num[bag_name] = int(num)
        except ValueError:
            bags[main_bag] = {}
            break
    bags[main_bag] = bags_with_num.copy()
    bags_with_num.clear()

pprint(bags, depth=2)

r = 0


def bfs(bag):
    if bag == 'shiny gold bag' or bag not in bags:
        return False
    que = {*bags[bag].keys()}
    while que:
        b = que.pop()
        if b == 'shiny gold bag' or (b in bags and 'shiny gold bag' in bags[b].keys()):
            return True
        elif b in bags:
            for k in bags[b].keys():
                que.add(k)
    return False


for b in bags.keys():
    if bfs(b):
        r += 1

print(r)

