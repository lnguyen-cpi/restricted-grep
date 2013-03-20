from string import ascii_letters
import sys

def match_asterisk(tosearch, pattern, escaped=False):
	""" Handles recursive aspect of the special asterisk case

		@param tosearch: string of characters where we look for the pattern
		@param pattern: string to match in the tosearch string.
		@param escaped: True if the character has no special value because it's been escaped.

	"""
	if len(pattern) == 0: #pattern found in search string
		return True
	if len(tosearch) == 0: #pattern not found in search string.
		return False

	if pattern[0] == "." and  (not escaped): #checks case where no char or extra char appears
		return match_asterisk(tosearch[1:], pattern) or control(tosearch[1:], pattern[2:])
	elif pattern[0] == tosearch[0]: #if current character is normal, try to match, then go deeper.
		return match_asterisk(tosearch[1:], pattern, True) or control(tosearch[1:], pattern[2:])
	else: 
		return control(tosearch, pattern[2:])

def control(tosearch, pattern):
	""" Handles decision making for the pattern matching.

		Examines a the first character in the current pattern string,
		then depending on its value goes to the appropriate matching case.
	
	"""
	if pattern == "": #all characters have been matched.
		return True
	if tosearch == "": # The pattern substring wasn't found in the line, so return false.
		if len(pattern) >= 2 and (pattern[0] != "\\" and pattern[1] == "*"):
			return True	#We look ahead to ensure that an asterisk doesn't affect results.
		return False
	if pattern[0] == "\\": #handles escape character
		if len(pattern) > 2:
			if pattern[2] == "*": #looks ahead to see if asterisk will apply
				return match_asterisk(tosearch, pattern[1:], True)
		else:
			if tosearch[0] == pattern[1]: # If not special case, match characters naively
				return control(tosearch[1:], pattern[2:])
			else:
				False

	elif len(pattern) > 1 and pattern[1] == "*": # Handles the asterisk special case.
		if len(pattern) > 1:
			return control(tosearch, pattern[2:]) or match_asterisk(tosearch, pattern)
		else:
			return control(tosearch, "")

	elif  pattern[0] == ".": # Handles the dot special case.  The empty string will be caught before this.
		return control(tosearch[1:], pattern[1:])

	elif pattern[0] == tosearch[0]:# Matches normal characters
		return control(tosearch[1:], pattern[1:])
	else:
		return False

def rgrep_matches(input_file, pattern):
	""" A restriced implementation of grep. Checks if pattern (type: string) is
		a substring of tosearch (type: string).

		Attempt to match the pattern using every character in the input line
		as a potential starting point.  If a character matches, then we pop 
		that character off the front of both the tosearch and pattern strings.
		We then call control() recursively.If the pattern string is empty, then 
		we've matched all characters (and popped all off our pattern string.)
		If the source string is empty, but the pattern isn't, then the entire
		pattern is not contained in that particular substring of the line to be
		searched.

		Special character values:
			* -> can match any character
			. -> the preceding character may appear 0 or more times.
			\ -> Nullifies any special meaning of the following character.
		All other characters have no special values

	"""
	text_file = open(input_file, 'r') #input source file.
	tosearch = text_file.readline() #grab the first line

	while (tosearch != ""): #checks each line in text file.
		# Starts search pattern at next char in search line
		for i in range(len(tosearch)):
			if control(tosearch[i:], pattern):
				print(tosearch)
		tosearch = text_file.readline()


if __name__ == "__main__": #handles arguments from command line
	input_file = sys.argv[1]
	pattern = sys.argv[2]
	rgrep_matches(input_file, pattern)
