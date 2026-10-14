class Solution:
    import re
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += s
        return encoded_string
        #"HelloWorld"

    def decode(self, s: str) -> List[str]:
        decode_string = re.split(r'(?<=.)(?=[A-Z])',s)
        return decode_string





