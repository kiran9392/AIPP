7def format_name(full_name: str) -> str:
	"""Format a full name as "Last,First".

	- Trims leading/trailing whitespace.
	- Treats the last whitespace-separated token as the last name.
	- Joins any remaining leading tokens as the first name (preserves internal spaces).
	- Returns an empty string for empty input.

	Examples:
		"Jayanth kasarla" -> "kasarla,Jayanth"
		" kiran gundam"   -> "gundam,kiran"

	Args:
		full_name: full name string

	Returns:
		Formatted string "Last,First" (no space after comma). If only one
		name token is provided, returns that token unchanged.

	Raises:
		TypeError: if full_name is not a str.
	"""
	if not isinstance(full_name, str):
		raise TypeError("full_name must be a string")

	parts = full_name.strip().split()
	if not parts:
		return ""
	if len(parts) == 1:
		return parts[0]

	last = parts[-1]
	first = " ".join(parts[:-1])
	return f"{last},{first}"


if __name__ == '__main__':
	examples = [
		("Jayanth kasarla", "kasarla,Jayanth"),
		(" kiran gundam", "gundam,kiran"),
		("karthik darla", "darla,karthik"),
	]

	for inp, expected in examples:
		out = format_name(inp)
		print(f"{inp!r} -> {out}")
		assert out == expected, f"expected {expected!r}, got {out!r}"

	print("All tests passed.")

