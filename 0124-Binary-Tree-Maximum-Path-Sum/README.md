# 124. Binary Tree Maximum Path Sum

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Tree, Depth-First Search, Binary Tree  
**Link:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

---

## Problem
A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 3 * 104]`.
* `-1000 <= Node.val <= 1000`

---

## My Approach
This problem is tackled just like the diameter of a tree is calculated. We can just calculate the maximum path sum for each particular subtree and the maximum of that. Whenever the sum is negative for any of the left or right subtree, we don't consider it coz it would make the sum even worse. Hence, we take max of 0 and the max left sum and the max right sum. After that, we take max sum of the three combinations. 

## Complexity
- Time: O(N)
- Space: O(N)
