def iterative_factorial(n):
	assert isinstance(n, int), "Pre-condition failed: n must be an integer"
	assert n >= 0, "Pre-condition failed: n must be non-negative"

	count = 0
	fact = 1

	while count != n:
		assert 0 <= count <= n, "Invariant failed: count out of bounds"
		assert fact == _math_factorial(count), "Invariant failed: fact != count!"

		count = count + 1
		fact = fact * count

		assert 0 <= count <= n, "Invariant failed after update: count out of bounds"
		assert fact == _math_factorial(count), "Invariant failed after update: fact != count!"

	assert count == n, "Termination condition failed: count must equal n"
	assert fact == _math_factorial(n), "Post-condition failed: fact must equal n!"
	return fact


def _math_factorial(k):
	assert isinstance(k, int) and k >= 0, "k must be a non-negative integer"
	result = 1
	for x in range(1, k + 1):
		result *= x
	return result


def main():
	for value in [0, 1, 5, 7]:
		print(f"{value}! = {iterative_factorial(value)}")


if __name__ == "__main__":
	main()
