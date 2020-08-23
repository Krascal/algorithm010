# 毕业总结

## 数组、栈、队列
#### 复习了数组、链表、栈、队列的概念及典型例题
#### python中有很多list的自带功能，可以在较短的代码内实现想要的功能。

## 哈希表
### 概念
#### 根据关键码值(Key value)而直接进行访问的数据结构。
#### 通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
### 哈希碰撞
#### 不同的输入得到了同一个哈希值，就会发生"哈希碰撞"
## 树、二叉树、搜索树
### 概念
#### 二叉树是n个有限元素的集合，该集合或者为空、或者由一个称为根（root）的元素及两个不相交的、被分别称为左子树和右子树的二叉树组成，是有序树。当集合为空时，称该二叉树为空二叉树。在二叉树中，一个元素也称作一个结点
####  Linked List 是特殊化的 Tree Tree 是特殊化的 Graph
###  二叉树遍历 Pre-order/In-order/Post-order
#### 1.前序(Pre-order):根-左-右 2.中序(In-order):左-根-右 3.后序(Post-order):左-右-根
## 堆、二叉堆
### 堆的概念
#### 可以迅速找到一堆数中最大值或者最小值的结构
### 二叉堆性质
#### 通过完全二叉树来实现：
#### 是一棵完全树；树中任一节点的值总是>=其子节点的值。

## 回溯
#### 回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。

## 搜索 - 遍历
#### 每个节点都要访问一次
#### 每个节点仅仅要访问一次

#### 对于节点的访问顺序不限
- 深度优先:depth first search
- 广度优先:breadth first search

## 贪心算法
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优(即最有
利)的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不
能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行
选择，有回退功能。

## 动态规划和递归或者分治没有本质上的区别（关键看有误最优的子结构）
## 共性：找到重复子问题
## 差异性：最优子结构，中途可以淘汰次优解

学习笔记
# 字典树
## 基本结构
字典树，即 Trie 树，又称单词 查找树或键树，是一种树形结 构。典型应用是用于统计和排 序大量的字符串(但不仅限于 字符串)，所以经常被搜索引 擎系统用于文本词频统计。
它的优点是:最大限度地减少无谓的字符串比较，查询效率比哈希表高。
## 基本性质
1. 结点本身不存完整单词;
2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的 字符串;
3. 每个结点的所有子结点路径代表的字符都不相同。

## 核心思想
Trie 树的核心思想是空间换时间。 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

# 并查集
## 基本操作
• makeSet(s):建立一个新的并查集，其中包含 s 个单元素集合。

• unionSet(x, y):把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在
 的集合不相交，如果相交则不合并。

• find(x):找到元素 x 所在的集合的代表，该操作也可以用于判断两个元 素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

# 初级搜素
1. 朴素搜索
2. 优化方式:不重复(fibonacci)、剪枝(生成括号问题)
3. 搜索方向:
DFS: depth first search 深度优先搜索 BFS: breadth first search 广度优先搜索
双向搜索、启发式搜索

# 回溯法
回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚
至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。
回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况: 

• 找到一个可能存在的正确的答案

• 在尝试了所有可能的分步方法后宣告该问题没有答案 在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

# 估价函数
启发式函数: h(n)，它用来评价哪些结点最有希望的是一个我们要找的结 点，h(n) 会返回一个非负实数,也可以认为是从结点n的目标结点路径的估 计成本。
启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。

# 二叉树遍历
 1. 前序(Pre-order):根-左-右 
 2. 中序(In-order):左-根-右 
 3. 后序(Post-order):左-右-根
 
# 二叉搜索树 Binary Search Tree
二叉搜索树，也称二叉搜索树、有序二叉树(Ordered Binary Tree)、排 序二叉树(Sorted Binary Tree)，是指一棵空树或者具有下列性质的二叉 树:
1. 左子树上所有结点的值均小于它的根结点的值;
2. 右子树上所有结点的值均大于它的根结点的值;
3. 以此类推:左、右子树也分别为二叉查找树。 (这就是 重复性!)
中序遍历:升序排列

# AVL 树
1. 发明者 G. M. Adelson-Velsky 和 Evgenii Landis
2. Balance Factor(平衡因子): 是它的左子树的高度减去它的右子树的高度(有时相反)。 balancefactor={-1, 0, 1}
3. 通过旋转操作来进行平衡(四种)

# 旋转操作
1. 左旋 2. 右旋 3. 左右旋 4. 右左旋

 子树形态:右右子树 —>左旋
 子树形态：左左子树 ->右旋
 子树形态：左右子树 ->左右旋
 子树形态：右左子树 ->右左旋
 
# AVL 总结
1. 平衡二叉搜索树
2. 每个结点存balancefactor={-1,0,1} 3. 四种旋转操作
不足:结点需要存储额外信息、且调整次数频繁

# Red-black Tree
红黑树是一种近似平衡的二叉搜索树(Binary Search Tree)，它能够确保任何一 个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉搜索树:

• 每个结点要么是红色，要么是黑色

• 根结点是黑色

• 每个叶结点(NIL结点，空结点)是黑色的。

• 不能有相邻接的两个红色结点

• 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。

# 关键性质
从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

学习笔记
## 指定位置的位运算
1. 将x最右边的n位清零:x&(~0<<n)
2. 获取x的第n位值(0或者1):(x>>n)&1
3. 获取x的第n位的幂值:x&(1<<n)
4. 仅将第n位置为1:x|(1<<n)
5. 仅将第n位置为0:x&(~(1<<n))
6. 将x最高位至第n位(含)清零:x&((1<<n)-1)
7. 将第n位至第0位(含)清零:x&(~((1<<(n+1))-1))

## 实战位运算要点
• 判断奇偶:
x%2==1 —>(x&1)==1 x%2==0 —>(x&1)==0
• x>>1—>x/2.
即: x=x/2; —> x=x>>1;
mid=(left+right)/2; —> mid=(left+right)>>1;
• X=X&(X-1)清零最低位的1
• X&-X=>得到最低位的 1
• X&~X=>0

## Bloom Filter vs Hash Table
一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索
一个元素是否在一个集合中。
优点是空间效率和查询时间都远远超过一般的算法，
缺点是有一定的误识别率和删除困难。

学习笔记

动态规划 和 递归或者分治 没有根本上的区别(关键看有无最优的子结构) 拥有共性:找到重复子问题
差异性:最优子结构、中途可以淘汰次优解。

# Rabin-Karp 算法
在朴素算法中，我们需要挨个比较所有字符，才知道目标字符串中是否包含子串。那么，是否有别的方法可以用来判断目标字符串是否包含子串呢?
答案是肯定的，确实存在一种更快的方法。为了避免挨个字符对目标字符串和子串进行比较，我们可以尝试一次性判断两者是否相等。因此，我们需要一个好的哈希函数(hash function)。 通过哈希函数，我们可以算出子 串的哈希值，然后将它和目标字符串中的子串的哈希值进行比较。 这个新方法在速度上比暴力法有显著提升。

# KMP 算法
KMP算法(Knuth-Morris-Pratt)的思想就是，当子串与目标字符串不匹配时， 其实你已经知道了前面已经匹配成功那 一部分的字符(包括子串与目标字符 串)。以阮一峰的文章为例，当空格与 D 不匹配时，你其实 知道前面六个字符是 “ABCDAB”。KMP 算法的想法是，设法利用这个已知信息，不要把“搜索位置” 移回已经比较过的位置，继续把它向后移，这样就提高了效率。