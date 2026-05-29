# LeetCode Algorithm Templates

> Quick-reference patterns. Read the description, copy the template, adapt variable names.

---

## Table of Contents
1. [Two Pointers](#1-two-pointers)
2. [Sliding Window](#2-sliding-window)
3. [Binary Search](#3-binary-search)
4. [BFS (Breadth-First Search)](#4-bfs-breadth-first-search)
5. [DFS (Depth-First Search)](#5-dfs-depth-first-search)
6. [Backtracking](#6-backtracking)
7. [Dynamic Programming — 1D](#7-dynamic-programming--1d)
8. [Dynamic Programming — 2D](#8-dynamic-programming--2d)
9. [Merge Intervals](#9-merge-intervals)
10. [Linked List — Fast & Slow Pointers](#10-linked-list--fast--slow-pointers)
11. [Monotonic Stack](#11-monotonic-stack)
12. [Heap / Priority Queue](#12-heap--priority-queue)
13. [Trie](#13-trie)
14. [Union-Find (Disjoint Set)](#14-union-find-disjoint-set)
15. [Topological Sort](#15-topological-sort)
16. [Bit Manipulation](#16-bit-manipulation)
17. [Prefix Sum](#17-prefix-sum)
18. [Matrix BFS / DFS (Grid)](#18-matrix-bfs--dfs-grid)

---

## 1. Two Pointers

**When to use:** Sorted array, pair/triplet sum, palindrome check, comparing from both ends.

**Time:** O(n) | **Space:** O(1)

```python
def two_pointers(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return [left, right]          # found answer
        elif current < target:
            left += 1                     # need bigger sum
        else:
            right -= 1                    # need smaller sum

    return -1
```

**Key signals:** "sorted array", "find pair that sums to X", "remove duplicates in-place"

---

## 2. Sliding Window

**When to use:** Contiguous subarray/substring with a constraint (max, min, exact count).

**Time:** O(n) | **Space:** O(1) fixed window, O(k) for variable window with a hashmap

### Fixed-size window
```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]   # slide: add right, remove left
        best = max(best, window_sum)

    return best
```

### Variable-size window (shrink when invalid)
```python
def variable_window(s):
    counts = {}
    left = 0
    best = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1   # expand right

        while not valid(counts):                           # shrink left until valid
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        best = max(best, right - left + 1)

    return best
```

**Key signals:** "longest/shortest subarray", "substring with at most k distinct", "minimum window"

---

## 3. Binary Search

**When to use:** Sorted input, "find minimum/maximum that satisfies condition", search space is monotonic.

**Time:** O(log n) | **Space:** O(1)

### Standard (find exact target)
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2   # avoids overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### Find leftmost valid position (bisect_left pattern)
```python
def binary_search_left(nums, target):
    left, right = 0, len(nums)   # right = len (open interval)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid           # keep mid in search space

    return left   # insertion point
```

### Binary search on answer
```python
def search_on_answer(lo, hi):
    # lo/hi are the possible answer range, not array indices
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid              # try smaller
        else:
            lo = mid + 1         # need bigger

    return lo   # minimum valid answer
```

**Key signals:** "sorted", "rotated sorted array", "minimum days/speed/capacity", "find peak"

---

## 4. BFS (Breadth-First Search)

**When to use:** Shortest path in unweighted graph, level-order traversal, "minimum steps".

**Time:** O(V + E) | **Space:** O(V)

### Graph BFS
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        # process node here

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### BFS — shortest path with distance tracking
```python
from collections import deque

def bfs_shortest(graph, start, end):
    visited = set([start])
    queue = deque([(start, 0)])   # (node, distance)

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1   # not reachable
```

### BFS — level by level
```python
from collections import deque

def bfs_levels(root):
    if not root:
        return []
    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):       # snapshot current level size
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)

    return result
```

**Key signals:** "shortest path", "level order", "minimum number of steps", "word ladder"

---

## 5. DFS (Depth-First Search)

**When to use:** Explore all paths, connected components, cycle detection, tree problems.

**Time:** O(V + E) | **Space:** O(V) call stack

### Recursive DFS on graph
```python
def dfs(graph, node, visited):
    visited.add(node)
    # process node here

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Call: dfs(graph, start, set())
```

### Iterative DFS (avoids recursion limit)
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        # process node here

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### DFS on binary tree
```python
def dfs_tree(node):
    if not node:
        return base_value

    left  = dfs_tree(node.left)
    right = dfs_tree(node.right)

    return combine(left, right, node.val)
```

**Key signals:** "all paths", "number of islands", "connected components", "detect cycle"

---

## 6. Backtracking

**When to use:** Generate all combinations/permutations/subsets, constraint satisfaction.

**Time:** O(2^n) or O(n!) | **Space:** O(n) recursion depth

```python
def backtrack(candidates, start, current, result, target):
    if base_case_met(current, target):
        result.append(list(current))    # snapshot — do NOT append current directly
        return

    for i in range(start, len(candidates)):
        if candidates[i] > target:      # pruning: skip impossible branches
            break

        current.append(candidates[i])
        backtrack(candidates, i + 1, current, result, target - candidates[i])
        current.pop()                   # undo choice (backtrack)

result = []
backtrack(candidates, 0, [], result, target)
```

### Permutations variant
```python
def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(list(current))
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return result
```

**Key signals:** "all combinations", "all permutations", "subsets", "N-Queens", "word search"

---

## 7. Dynamic Programming — 1D

**When to use:** Optimal substructure + overlapping subproblems on a 1D sequence.

**Time:** O(n) | **Space:** O(n) → can often reduce to O(1)

```python
def dp_1d(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = base_case

    for i in range(1, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])   # adapt recurrence to problem

    return dp[-1]

# Space-optimized (if only need last 1-2 states):
prev2, prev1 = 0, 0
for num in nums:
    prev2, prev1 = prev1, max(prev1, prev2 + num)
return prev1
```

**Common recurrences:**
- House Robber: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
- Climbing Stairs: `dp[i] = dp[i-1] + dp[i-2]`
- Max Subarray (Kadane's): `dp[i] = max(nums[i], dp[i-1] + nums[i])`

**Key signals:** "max profit", "minimum cost", "number of ways", "can you reach the end"

---

## 8. Dynamic Programming — 2D

**When to use:** Two sequences (LCS, edit distance), grid paths, knapsack variants.

**Time:** O(m×n) | **Space:** O(m×n) → often reducible to O(n)

```python
def dp_2d(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1): dp[i][0] = i   # adjust per problem
    for j in range(n + 1): dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # delete
                                   dp[i][j-1],    # insert
                                   dp[i-1][j-1])  # replace

    return dp[m][n]
```

**Common problems:** Edit Distance, LCS, Longest Palindromic Subsequence, 0/1 Knapsack, Coin Change 2

**Key signals:** "two strings", "grid paths", "choose items with weight/value constraint"

---

## 9. Merge Intervals

**When to use:** Overlapping ranges, scheduling, calendar problems.

**Time:** O(n log n) sort + O(n) merge | **Space:** O(n)

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])   # sort by start
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                      # overlapping
            merged[-1][1] = max(merged[-1][1], end)    # extend
        else:
            merged.append([start, end])                 # no overlap, add new

    return merged
```

### Insert interval
```python
def insert_interval(intervals, new):
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new[0]:   # before new
        result.append(intervals[i]); i += 1

    while i < n and intervals[i][0] <= new[1]:  # overlapping — merge
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    result.append(new)

    while i < n:                                  # after new
        result.append(intervals[i]); i += 1

    return result
```

**Key signals:** "merge overlapping intervals", "meeting rooms", "insert interval"

---

## 10. Linked List — Fast & Slow Pointers

**When to use:** Detect cycle, find middle, find Nth node from end.

**Time:** O(n) | **Space:** O(1)

```python
def fast_slow(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:           # cycle detected
            return True

    return False   # no cycle; slow is now at middle if no cycle
```

### Find middle of linked list
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # middle node
```

### Reverse a linked list
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**Key signals:** "detect cycle", "middle of list", "palindrome linked list", "reorder list"

---

## 11. Monotonic Stack

**When to use:** Next greater/smaller element, largest rectangle, trapping rain water.

**Time:** O(n) | **Space:** O(n)

### Next Greater Element
```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []   # stores indices, maintains decreasing order of values

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num           # num is the next greater for idx
        stack.append(i)

    return result
```

### Largest Rectangle in Histogram
```python
def largest_rectangle(heights):
    stack = []   # (index, height) — monotonically increasing
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area
```

**Key signals:** "next greater/smaller", "daily temperatures", "largest rectangle", "rain water"

---

## 12. Heap / Priority Queue

**When to use:** Kth largest/smallest, merge K sorted lists, running median.

**Time:** O(n log k) | **Space:** O(k)

```python
import heapq

# Min-heap (default in Python)
heap = []
heapq.heappush(heap, val)
smallest = heapq.heappop(heap)

# Max-heap: negate values
heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)

# Kth largest element
def kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)   # evict smallest, keep top-k
    return heap[0]

# Merge K sorted lists
def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))   # (val, list_idx, element_idx)

    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j+1], i, j+1))

    return result
```

**Key signals:** "Kth largest/smallest", "top K frequent", "merge K lists", "median from stream"

---

## 13. Trie

**When to use:** Prefix matching, autocomplete, word search in a dictionary.

**Time:** O(m) per insert/search (m = word length) | **Space:** O(total chars)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

**Key signals:** "prefix", "autocomplete", "word dictionary", "replace words"

---

## 14. Union-Find (Disjoint Set)

**When to use:** Connected components, detect cycle in undirected graph, Kruskal's MST.

**Time:** O(α(n)) ≈ O(1) amortized per operation | **Space:** O(n)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False   # already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px                              # union by rank
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Usage
uf = UnionFind(n)
for u, v in edges:
    if not uf.union(u, v):
        # u and v were already connected → cycle detected
        pass
```

**Key signals:** "number of connected components", "redundant connection", "accounts merge"

---

## 15. Topological Sort

**When to use:** Ordering tasks with dependencies (DAG), course schedule, build order.

**Time:** O(V + E) | **Space:** O(V + E)

### Kahn's Algorithm (BFS-based)
```python
from collections import deque

def topo_sort(n, prerequisites):
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for dst, src in prerequisites:
        graph[src].append(dst)
        in_degree[dst] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []   # empty = cycle exists
```

### DFS-based
```python
def topo_sort_dfs(n, prerequisites):
    graph = [[] for _ in range(n)]
    for dst, src in prerequisites:
        graph[src].append(dst)

    visited = [0] * n   # 0=unvisited, 1=visiting, 2=done
    order = []

    def dfs(node):
        if visited[node] == 1: return False   # cycle
        if visited[node] == 2: return True
        visited[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor): return False
        visited[node] = 2
        order.append(node)
        return True

    for i in range(n):
        if visited[i] == 0 and not dfs(i):
            return []   # cycle

    return order[::-1]
```

**Key signals:** "course schedule", "task ordering", "build order", "detect cycle in directed graph"

---

## 16. Bit Manipulation

**When to use:** XOR tricks, counting bits, subset generation, power of 2 checks.

**Time:** O(1) or O(n) | **Space:** O(1)

```python
# Common operations
x & 1            # check if odd (last bit)
x >> 1           # divide by 2
x << 1           # multiply by 2
x & (x - 1)      # clear lowest set bit (checks power of 2 when result == 0)
x & (-x)         # isolate lowest set bit
x ^ x == 0       # x XOR itself = 0 (find single number in pairs)
~x               # bitwise NOT

# Count set bits (Brian Kernighan)
def count_bits(n):
    count = 0
    while n:
        n &= n - 1   # clear lowest bit each iteration
        count += 1
    return count

# Find single number (all others appear twice)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num   # XOR cancels duplicates
    return result

# Generate all subsets using bitmask
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):   # 0 to 2^n - 1
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result
```

**Key signals:** "single number", "power of 2", "count bits", "subsets", "XOR"

---

## 17. Prefix Sum

**When to use:** Range sum queries, subarray sum equals k, 2D range queries.

**Time:** O(n) build + O(1) query | **Space:** O(n)

```python
# 1D prefix sum
def prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i, num in enumerate(nums):
        prefix[i+1] = prefix[i] + num
    # range sum [l, r] (0-indexed, inclusive):
    # prefix[r+1] - prefix[l]
    return prefix

# Subarray sum equals k (uses hashmap of prefix sums)
def subarray_sum_k(nums, k):
    count = 0
    curr_sum = 0
    seen = {0: 1}   # prefix_sum → frequency

    for num in nums:
        curr_sum += num
        count += seen.get(curr_sum - k, 0)   # how many prefixes sum to curr-k
        seen[curr_sum] = seen.get(curr_sum, 0) + 1

    return count
```

**Key signals:** "range sum", "subarray sum equals k", "running total", "2D matrix sum"

---

## 18. Matrix BFS / DFS (Grid)

**When to use:** Number of islands, shortest path in a grid, flood fill, "4 directions".

**Time:** O(m×n) | **Space:** O(m×n)

```python
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]   # right, left, down, up

def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

# BFS on grid (shortest path)
from collections import deque

def bfs_grid(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    visited = set([(start_r, start_c)])
    queue = deque([(start_r, start_c, 0)])   # (row, col, distance)

    while queue:
        r, c, dist = queue.popleft()

        if is_target(r, c, grid):
            return dist

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, rows, cols) and (nr, nc) not in visited and grid[nr][nc] != WALL:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1

# DFS on grid (e.g., number of islands / flood fill)
def dfs_grid(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    if not in_bounds(r, c, rows, cols) or grid[r][c] != '1':
        return

    grid[r][c] = '0'   # mark visited (mutate grid to avoid extra set)

    for dr, dc in DIRECTIONS:
        dfs_grid(grid, r + dr, c + dc)

def num_islands(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs_grid(grid, r, c)
                count += 1
    return count
```

**Key signals:** "number of islands", "flood fill", "shortest path in grid", "walls and gates"

---

## Quick-Pick Guide

| Pattern | Trigger words |
|---|---|
| Two Pointers | sorted, pair sum, palindrome, in-place remove |
| Sliding Window | subarray/substring, longest/shortest, at most k |
| Binary Search | sorted, find min/max satisfying condition |
| BFS | shortest path, level order, minimum steps |
| DFS | all paths, connected components, tree traversal |
| Backtracking | all combinations/permutations/subsets |
| DP 1D | max/min over sequence, number of ways |
| DP 2D | two strings, grid paths, knapsack |
| Merge Intervals | overlapping ranges, scheduling |
| Fast & Slow Pointers | cycle detection, middle of list |
| Monotonic Stack | next greater/smaller, histogram |
| Heap | Kth element, top K, merge K lists |
| Trie | prefix, autocomplete, word dictionary |
| Union-Find | connected components, detect cycle (undirected) |
| Topological Sort | dependencies, course schedule, directed cycle |
| Bit Manipulation | XOR, power of 2, subsets via bitmask |
| Prefix Sum | range sum, subarray sum = k |
| Grid BFS/DFS | islands, flood fill, shortest grid path |
