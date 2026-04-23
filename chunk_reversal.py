def reverse_chunk_order(a, k):
    assert isinstance(a, list), "Pre-condition failed: a must be a list"
    assert isinstance(k, int), "Pre-condition failed: k must be an integer"
    n = len(a)
    assert n >= 2, "Pre-condition failed: list length n must be at least 2"
    assert 1 < k < n, "Pre-condition failed: require 1 < k < n"

    original = a.copy()

    # Chunk decomposition allows a final chunk with size < k when n is not divisible by k.
    chunks = [a[i:i + k] for i in range(0, n, k)]
    reversed_chunks = list(reversed(chunks))

    result = []
    i = 0
    m = len(reversed_chunks)

    # Loop invariant:
    # result equals the concatenation of reversed_chunks[0:i],
    # and each relocated chunk preserves its internal relative order.
    while i < m:
        expected_prefix = [x for ch in reversed_chunks[:i] for x in ch]
        assert result == expected_prefix, "Invariant failed: result prefix is incorrect"

        current_chunk = reversed_chunks[i]
        assert current_chunk == chunks[m - 1 - i], "Invariant failed: wrong chunk selected"

        result.extend(current_chunk)
        i += 1

        expected_prefix_after = [x for ch in reversed_chunks[:i] for x in ch]
        assert result == expected_prefix_after, "Invariant failed after update: prefix mismatch"

    # Post-conditions
    expected = [x for ch in reversed_chunks for x in ch]
    assert result == expected, "Post-condition failed: chunk order not reversed correctly"
    assert len(result) == n, "Post-condition failed: length changed"
    assert sorted(result) == sorted(original), "Post-condition failed: elements changed"

    # Strong post-condition: every chunk's internal order is preserved
    # by construction because we only move whole slices without reordering them.
    return result


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    print("Input :", data)
    print("Output:", reverse_chunk_order(data, k))

    data2 = [1, 2, 3, 4, 5, 6, 7]
    k2 = 3
    print("Input :", data2)
    print("Output:", reverse_chunk_order(data2, k2))


if __name__ == "__main__":
    main()
