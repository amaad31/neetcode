class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        len_strs = len(strs)
        output = []
        dict_list = []
        for i, curr_str in enumerate(strs):
            curr_dict = {}
            anagram_present = False
            for curr_str_ch in curr_str:
                curr_dict[curr_str_ch] = curr_dict.get(curr_str_ch, 0) + 1
            for j, curr_dict_list in enumerate(dict_list):
                if curr_dict_list == curr_dict:
                    output[j].append(curr_str)
                    anagram_present = True
            if not anagram_present:
                output.append([curr_str])
                dict_list.append(curr_dict)
        return output
                