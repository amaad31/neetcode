class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for cur_str in strs:
            encoded_str += "!#," + str(len(cur_str)) + ",!" + cur_str
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            if "!" == s[i] and "#" == s[i + 1] and "," == s[i + 2]:
                i += 3
                read_len = ""
                while True:
                    if "," == s[i] and "!" == s[i + 1]:
                        break
                    read_len += s[i]
                    i += 1
                i += 2
                
                decode_string = s[i: i + int(read_len)]
                decoded_str.append(decode_string)
                i += int(read_len)
            else:
                i += 1
        
        return decoded_str