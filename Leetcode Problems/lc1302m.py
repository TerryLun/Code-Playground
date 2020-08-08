def deepestLeavesSum(root):
    q = [root]
    while q:
        last_level, q = q, [child for node in q for child in [node.left, node.right] if child]
    return sum(node.val for node in last_level)
