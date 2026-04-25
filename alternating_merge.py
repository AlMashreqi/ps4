def alternating_merge(l1, l2):

    assert isinstance(l1, list), "Pre-condition failed: l1 must be a list"
    assert isinstance(l2, list), "Pre-condition failed: l2 must be a list"

    n1 = len(l1)
    n2 = len(l2)

    result = []
    i = 0

    while i < min(n1, n2):
        assert 0 <= i <= min(n1, n2), "Invariant failed: i out of valid range"

        expected_prefix = []
        for t in range(i):
            expected_prefix.append(l1[t])
            expected_prefix.append(l2[t])
        assert result == expected_prefix, "Invariant failed: result prefix is incorrect"

        result.append(l1[i])
        result.append(l2[i])
        i += 1

        expected_prefix_after = []
        for t in range(i):
            expected_prefix_after.append(l1[t])
            expected_prefix_after.append(l2[t])
        assert result == expected_prefix_after, "Invariant failed after update: prefix mismatch"

    if n1 > n2:
        result.extend(l1[i:])
    else:
        result.extend(l2[i:])

    # bruh
    assert len(result) == n1 + n2, "Post-condition failed: output length mismatch"

    expected = []
    m = min(n1, n2)
    for t in range(m):
        expected.append(l1[t])
        expected.append(l2[t])
    if n1 > n2:
        expected.extend(l1[m:])
    else:
        expected.extend(l2[m:])

    assert result == expected, "Post-condition failed: result is not a correct interleaving"
    return result


def main():
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8]
    print("Equal lengths:")
    print("L1:", a)
    print("L2:", b)
    print("Merged:", alternating_merge(a, b))

    c = [10, 20, 30, 40, 50]
    d = [11, 21]
    print("\nUnequal lengths:")
    print("L1:", c)
    print("L2:", d)
    print("Merged:", alternating_merge(c, d))


if __name__ == "__main__":
    main()
