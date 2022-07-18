import re

class DigitRetrieve:

	def __call__(self,string,*args, **kwargs):
		if string[0] == "-":
			if string[1:].isdigit():
				return int(string)
		elif string.isdigit():
			return (int(string))
		return None




class DigitRetrieve:
    def __call__(self, string):
        return int(string) if re.fullmatch('-?\d+', string) is not None else None


class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        pattern = r'^[+-]?\d+$'
        if match(pattern, args[0]):
            return int(args[0])
        return None