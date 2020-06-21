# 给定一个 N 叉树，返回其节点值的前序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其前序遍历: [1,3,5,6,2,4]。
#
#
#
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]  # 初始化一个数据
        out = []
        while stack:
            temp = stack.pop()  # 先把栈顶的数据弹出来加入到 输出 集
            out.append(temp.val)
            if temp.children:  # 如果该元素有子节点children 则反转加入到 stack 里(因为是前序遍历)
                for item in temp.children[::-1]:
                    stack.append(item)
        return out

# leetcode submit region end(Prohibit modification and deletion)
