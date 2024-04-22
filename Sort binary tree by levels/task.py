def tree_by_levels(node):
    if node is None:
        return []
    res = []
    current = [node]
    while current:
        next = []
        for node in current:
            res.append(node.value)
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
        current = next
    return res
