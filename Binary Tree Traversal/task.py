# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    res = [node.data]
    res.extend(pre_order(node.left))
    res.extend(pre_order(node.right))
    return res

# In-order traversal
def in_order(node):
    return []

# Post-order traversal
def post_order(node):
    return []

