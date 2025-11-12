def is_leap_year(year: int) -> bool:
	"""Return True if `year` is a leap year in the Gregorian calendar.

	Rules:
	- Every year divisible by 4 is a leap year,
	  except years divisible by 100 are not leap years,
	  unless they are also divisible by 400.

	Args:
		year: The year to check (integer).

	Returns:
		True if `year` is a leap year, False otherwise.

	Raises:
		TypeError: If `year` is not an int.
	"""
	if not isinstance(year, int):
		raise TypeError("year must be an integer")

	if year % 4 != 0:
		return False
	if year % 100 != 0:
		return True
	return year % 400 == 0


if __name__ == '__main__':
	# sample years and expected results
	sample_years = [2000, 1900, 2004, 2001, 2400]
	for y in sample_years:
		print(f"{y}: {is_leap_year(y)}")

	# quick assertions (simple tests)
	assert is_leap_year(2000) is True
	assert is_leap_year(1900) is False
	assert is_leap_year(2004) is True
	assert is_leap_year(2001) is False

	print("All tests passed.")


