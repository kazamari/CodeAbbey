'''
You are to create binary ordered tree from sequence of numbers as explained above (without caring of rebalancing it).
For each next number simply find the place where it should be inserted and add it there.

To represent the output, use the following format:

    each node is written as (left,value,right);
    the value is always a number;
    branches left and right could be empty, which is specified with dash -;
    if branch is not empty, it should contain another node.

The tree from the picture above will be represented as:

((-,2,-),3,((-,4,-),5,(-,8,-)))

Input data will contain the length of array which should be converted to tree.
The next line will contain the array itself - integers, separated by spaces.
Answer should contain the tree description in the format specified above.

Example:

input data:
5
3 5 4 2 8

output data:
((-,2,-),3,((-,4,-),5,(-,8,-)))
'''


def tree_to_string(node):
    left, root, right = node
    left = tree_to_string(left) if left else '-'
    right = tree_to_string(right) if right else '-'
    return '({},{},{})'.format(left, root, right)


def add_node(node, value):
    left, root, right = node
    if value > root:
        right = add_node(right, value) if right else (None, value, None)
    else:
        left = add_node(left, value) if left else (None, value, None)
    return left, root, right


def build_tree(array):
    tree = (None, array[0], None)
    for value in array[1:]:
        tree = add_node(tree, value)
    return tree_to_string(tree)


n = int(input())
print(build_tree([int(x) for x in input().split()]))