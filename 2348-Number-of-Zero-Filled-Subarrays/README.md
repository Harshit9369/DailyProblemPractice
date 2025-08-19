# 2348. Number of Zero-Filled Subarrays

**Difficulty:** Medium  
**Tags:** Array, Math  
**Link:** https://leetcode.com/problems/number-of-zero-filled-subarrays/

---

## Problem
Given an integer array `nums`, return *the number of **subarrays** filled with* `0`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

**Example 1:**

```
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

**Example 2:**

```
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
```

**Example 3:**

```
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
```

**Constraints:**

* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`

---

## My Approach
Simple Problem with just a mathematical approach where we have to just count the number of continuous zeroes at a time. The number of subarrays using those zeroes is (cnt * (cnt + 1)) / 2. Whenever encountered a non zero number, we can just make count as 0 and update the answer. 
The only edge case was when the array ended with 0. Easy to handle. 

## Complexity
- Time: O(N)
- Space: O(1)

## Alternate Approaches
(Outline other viable solutions and when to prefer them.)
The only approach which is the most efficient is already outlined above.

## Notes
(Add proofs, pitfalls, and follow-ups.)
None
