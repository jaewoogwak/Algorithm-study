
from typing import Optional, List
# Definition for a Node.


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root == None:
            return 0

        q = []
        depth = 0

        q.append(root)

        while len(q) > 0:
            size = len(q)

            temp = []
            for _ in range(size):
                currNode = q.pop()
                if currNode.children != None:
                    for ch in currNode.children:
                        temp.append(ch)

            q.extend(temp)

            depth += 1

        return depth


# Helper function to build the tree from an array
def build_tree(values: List[Optional[int]]) -> Optional[Node]:
    if not values:
        return None

    # 첫 번째 값으로 루트 노드 생성
    root = Node(values[0], [])
    queue = [root]
    i = 2  # 두 번째 값부터 처리 (첫 번째 값은 루트)

    while i < len(values):
        current = queue.pop(0)
        children = []
        # 자식 노드가 있는지 확인
        while i < len(values) and values[i] is not None:
            child_node = Node(values[i], [])
            children.append(child_node)
            queue.append(child_node)
            i += 1
        current.children = children
        i += 1  # None을 넘김

    return root


# Test case 1
values1 = [1, None, 3, 2, 4, None, 5, 6]
root1 = build_tree(values1)

solution = Solution()
print(f"Test case 1 output: {solution.maxDepth(root1)}")  # Output: 3

# Test case 2
values2 = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None,
           9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
root2 = build_tree(values2)

print(f"Test case 2 output: {solution.maxDepth(root2)}")  # Output: 5
