# 135. Candy 

### Mark

**Difficulty:** Hard  
**Tags:** Array, Greedy  
**Link:** https://leetcode.com/problems/candy/

---

## Problem
There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.

Return *the minimum number of candies you need to have to distribute the candies to the children*.

**Example 1:**

```
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

**Example 2:**

```
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
```

**Constraints:**

* `n == ratings.length`
* `1 <= n <= 2 * 104`
* `0 <= ratings[i] <= 2 * 104`

---

## My Approach
1. The first approach is to simply traverse from the left and store the value with respect to the left neighbor only. In the second traversal, we consider the right neighbor and then the sum is equal to the maximum of the right neighbor or the left neighbor.
2. The second approach is "Slope Concept" based. We don't consider the peeks in the array differently. If we are moving in an upward direction, we can just take one extra from the previous one. If moving in the downward direction, we start with 1 in this case too and just take one more than the previous one because what matters is taking the correct sum. If down > peak, then it means that the peak was supposed to be the down value. Therefore, we add an extra (down - peak) to the sum. 

## Complexity
- Time: O(N)
- Space: O(1)

## Notes
Great Problem! The first approach is doable but the second approach is a little bit tough to think about. Solve it again and try to grasp the concept and depth of the problem. 
- The problem shows how to think differently and how we can simply approach a difficult problem like this by just thinking a little out of the box. 

