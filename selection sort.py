def SelectionSort(a, l, r):
	# Pre-condition: valid subarray boundaries and established input array
	assert isinstance(a, list), "Pre-condition failed: a must be a list"
	assert isinstance(l, int) and isinstance(r, int), "Pre-condition failed: l and r must be integers"
	assert 0 <= l <= r < len(a), "Pre-condition failed: require 0 <= l <= r < len(a)"

	original_segment = a[l:r + 1].copy()

	i = l

	# Outer-loop invariant (before each iteration):
	# 1) a[l..i-1] is sorted in ascending order
	# 2) all a[l..i-1] <= all a[i..r]
	# 3) a[l..r] is a permutation of the original segment
	while i <= r:
		assert all(a[k] <= a[k + 1] for k in range(l, i - 1)), \
			"Outer invariant failed: sorted prefix violated"
		assert all(a[p] <= a[q] for p in range(l, i) for q in range(i, r + 1)), \
			"Outer invariant failed: prefix contains non-minimal value"
		assert sorted(a[l:r + 1]) == sorted(original_segment), \
			"Outer invariant failed: segment is not a permutation of original"

		p, j = i, i + 1

		# Inner-loop invariant (before each iteration):
		# p is index of minimum element in a[i..j-1], with i <= p <= j-1
		# and i+1 <= j <= r+1
		while j <= r:
			assert i <= p <= j - 1, "Inner invariant failed: p out of scanned bounds"
			assert all(a[p] <= a[t] for t in range(i, j)), \
				"Inner invariant failed: p is not minimum of scanned range"

			if a[j] < a[p]:
				p = j
			j += 1

		# After inner loop: p is minimum index in a[i..r]
		assert i <= p <= r, "Post-inner failed: p out of suffix bounds"
		assert all(a[p] <= a[t] for t in range(i, r + 1)), \
			"Post-inner failed: p is not minimum in unsorted suffix"

		# Place minimum at start of unsorted part
		a[p], a[i] = a[i], a[p]
		i += 1

	# Post-condition: a[l..r] sorted and still same multiset of elements
	assert all(a[k] <= a[k + 1] for k in range(l, r)), \
		"Post-condition failed: segment is not sorted"
	assert sorted(a[l:r + 1]) == sorted(original_segment), \
		"Post-condition failed: segment is not a permutation of input"




def main():
	A = [3, 2, 7, 1, 6]
	print("Before:", A)
	SelectionSort(A, 0, len(A) - 1)
	print("After: ", A)

if __name__ == '__main__':
	main()