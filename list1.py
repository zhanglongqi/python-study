__author__ = 'longqi'

l1 = [2, 6, 20, 4]
print(l1)

l1.insert(3, 9)
print(l1)


# using lists as stacks
l1.append(87)
print(l1)
print(l1.__len__())
print(l1.pop())
print(l1)
print(l1.__len__())

# using lists as queues
# l1.popleft()

"""
Slicing
Just as you use indexing to access individual elements, you can use slicingto access rangesof
elements.
The first index is the number of the first element you want to include.
However, the last index is the number of the first element after your slice.
"""

l1.append('ab')
l1.append('xyz')
print(l1)
print(l1[3:100], l1[1:4])
print(l1[-3:-1])
print(l1[3:], l1[:3])

print('\n***************\n')

l1 = [0.402, 5.01, 458, 201, 12345678901234567890]
normalizeLen = 16

print(l1)


def normalize_num(src):
    tar = []
    for i, d1 in enumerate(src):
        d1 = str(d1)
        print(len(d1))
        if len(d1) < normalizeLen:
            tar.append(' ' * (normalizeLen - len(d1)) + str(d1))
        elif len(d1) == normalizeLen:
            tar.append(str(d1))
        else:
            print('item: \"', d1, '\" index: \"', i, '\" too long...')
            tar.append(d1[:16])
    return tar


print(normalize_num(l1))

print('\n***************\n')

l1 = [1, 2, 3, 5, 6]
l2 = [5, 6, 7, 8, 9]

print(set(l1) & set(l2))

t1 = ('abc', 4)
print(t1[0], '\n\n', t1[1])
