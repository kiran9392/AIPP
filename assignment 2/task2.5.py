from typing import Iterable, Dict, Tuple, Union


Number = Union[int, float]


def sum_even_odd(
	numbers: Iterable[Number],
	*,
	allow_floats: bool = True,
	require_integer_floats: bool = True,
	strict: bool = False,
	return_tuple: bool = False,
) -> Union[Dict[str, int], Tuple[int, int]]:
	"""
	Calculate the sum of even and odd numbers from an iterable.

	Parameters
	----------
	numbers:
		Iterable of numbers (ints or floats). Non-numeric types are ignored by default.
	allow_floats:
		If True, float items are considered. If False, floats are skipped (or raise if strict).
	require_integer_floats:
		If True, only floats that are mathematically integers (e.g. 7.0) are accepted and
		converted to int. If False, non-integer floats are truncated via int(x).
	strict:
		If True, encountering a non-acceptable value (e.g. a float when allow_floats is False,
		or a non-numeric value) raises a ValueError. If False, such values are skipped.
	return_tuple:
		If True, return (even_sum, odd_sum) tuple. Else return dict {'even_sum':..., 'odd_sum':...}.

	Returns
	-------
	dict or tuple
		Either a dict with keys 'even_sum' and 'odd_sum' or a tuple (even_sum, odd_sum).

	Notes
	-----
	- Booleans are treated as integers (True == 1, False == 0).
	- This function intentionally accepts ints and floats only; other types are ignored unless
	  `strict=True`, in which case a ValueError is raised on the first invalid element.
	"""
	even_sum = 0
	odd_sum = 0

	for idx, x in enumerate(numbers):
		# Accept ints and floats only
		if isinstance(x, bool):
			# bool is subclass of int, keep that behavior
			n = int(x)
		elif isinstance(x, int):
			n = x
		elif isinstance(x, float):
			if not allow_floats:
				if strict:
					raise ValueError(f"Floats not allowed (index {idx}): {x}")
				else:
					continue
			# allow_floats == True
			if require_integer_floats:
				if x.is_integer():
					n = int(x)
				else:
					if strict:
						raise ValueError(f"Non-integer float encountered (index {idx}): {x}")
					else:
						# skip non-integer float
						continue
			else:
				# convert/truncate float to int
				n = int(x)
		else:
			# non-numeric
			if strict:
				raise ValueError(f"Non-numeric value encountered (index {idx}): {x}")
			else:
				continue

		if n % 2 == 0:
			even_sum += n
		else:
			odd_sum += n

	if return_tuple:
		return (even_sum, odd_sum)
	return {"even_sum": even_sum, "odd_sum": odd_sum}


if __name__ == '__main__':
	# Demo examples
	data1 = [1, 2, 3, 4, 5]
	print('data1 ->', data1)
	print('sums ->', sum_even_odd(data1))  # even_sum=6 (2+4), odd_sum=9 (1+3+5)

	data2 = [10, 'a', 7.0, 8, None, 3, 2.5]
	print('\nmixed data2 ->', data2)
	print('default (allow_floats=True, require_integer_floats=True) ->', sum_even_odd(data2))
	print('allow non-integer floats (truncate) ->', sum_even_odd(data2, allow_floats=True, require_integer_floats=False))
	try:
		print('strict mode (raises on invalid) ->', sum_even_odd(data2, strict=True))
	except ValueError as e:
		print('strict mode raised:', e)

	# Return tuple example
	print('\nreturn tuple ->', sum_even_odd([2, 3, 4], return_tuple=True))
