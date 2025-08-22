# 543. Diameter of Binary Tree

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Binary Tree  
**Link:** https://leetcode.com/problems/diameter-of-binary-tree/

---

## Problem
Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-100 <= Node.val <= 100`

---

## My Approach
To find the diameter of the tree, we have to take the max of every possible left height from a node and the right height from a node. For that, the easiest way is to track the left height and right height from the root and check for each node going left and right. 

## Complexity
- Time: O(N)
- Space: O(N) -> Auxiliary Stack Space. 

## Alternate Approaches
Other approach can be the simple O(N^2) approach where we can just find the diameter from every possible node.
