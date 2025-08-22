# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree  
**Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

---

## Problem
Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 104]`.
* `-100 <= Node.val <= 100`

---

## My Approach
Take the maximum of both the left subtree and the right subtree and add 1 to the result. 

## Complexity
- Time: O(N)
- Space: O(N) -> Auxiliary Stack Space

