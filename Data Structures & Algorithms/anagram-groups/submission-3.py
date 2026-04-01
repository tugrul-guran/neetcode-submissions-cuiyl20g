class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_to_index = {}
        result = []
        current_index = 0

        for word in strs:
            s_word = "".join(sorted(word))

            if s_word not in word_to_index:

                word_to_index[s_word] = current_index
                current_index += 1
                result.append([])

            result[word_to_index[s_word]].append(word)

        return result