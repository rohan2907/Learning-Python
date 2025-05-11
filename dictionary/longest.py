## Find the longest and shortest meaning in a dictionary

d = {
    'piece': 'portion of an object or of material, produced by cutting',
    'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
    'area': 'a region or a parth of a town, a country, or the world',
    'visit': 'go to see and spend time with (someone)',
    'with': 'having or possessing',
    'small': 'less than normal'
}

keys = list(d.keys())
values = list(d.values())
lenght = [ len(x) for x in values]
max_len = max(lenght)
min_len = min(lenght)

max_index = lenght.index(max_len)
min_index = lenght.index(min_len)

print('Max => {} : {}'.format(keys[max_index], values[max_index]))
print('Min => {} : {}'.format(keys[min_index], values[min_index]))
