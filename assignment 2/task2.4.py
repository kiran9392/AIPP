import re
from typing import Iterable, Optional, Union


def sum_of_squares(iterable: Optional[Iterable[Union[int, float]]] = None,
				   start: Optional[int] = None,
				   end: Optional[int] = None) -> float:
	"""
	Compute the sum of squares.

	Usage modes (mutually exclusive):
	  - iterable provided: sum of x*x for each numeric x in iterable
	  - start and end provided (integers): sum of i*i for i in range(start, end+1)

	Args:
		iterable: optional iterable of numbers (ints or floats)
		start: optional start integer (inclusive) when using range mode
		end: optional end integer (inclusive) when using range mode

	Returns:
		Sum of squares as a float (or int-like float when values are integers).

	Raises:
		ValueError: if arguments are invalid or mutually ambiguous.
	"""
	# Validate modes
	if iterable is not None and (start is not None or end is not None):
		raise ValueError("Provide either 'iterable' OR 'start'/'end', not both.")

	if iterable is None:
		# range mode required both start and end
		if start is None or end is None:
			raise ValueError("When 'iterable' is not provided, both 'start' and 'end' must be given.")
		# ensure integers
		if not (isinstance(start, int) and isinstance(end, int)):
			raise ValueError("'start' and 'end' must be integers")
		# handle empty/invalid ranges gracefully
		if end < start:
			return 0.0
		total = 0
		for i in range(start, end + 1):
			total += i * i
		return float(total)

	# iterable mode
	total = 0.0
	for x in iterable:
		try:
			n = float(x)
		except Exception:
			# skip non-numeric entries
			continue
		total += n * n
	return total


if __name__ == '__main__':
	# Examples / quick tests
	print('sum_of_squares(iterable=[1,2,3]) ->', sum_of_squares(iterable=[1, 2, 3]))  # 1+4+9 = 14
	print("sum_of_squares(start=1, end=3) ->", sum_of_squares(start=1, end=3))      # 1+4+9 = 14
	print("sum_of_squares(iterable=[1.5,2]) ->", sum_of_squares(iterable=[1.5, 2]))  # 2.25 + 4 = 6.25
	print("sum_of_squares(start=5, end=3) ->", sum_of_squares(start=5, end=3))      # end < start -> 0.0
