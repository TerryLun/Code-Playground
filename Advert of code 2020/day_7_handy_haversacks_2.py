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


def bag_dive(bag):
    r = 0
    for k, v in bags[bag].items():
        r += v + v * bag_dive(k)
    return r


print(bag_dive('shiny gold bag'))
