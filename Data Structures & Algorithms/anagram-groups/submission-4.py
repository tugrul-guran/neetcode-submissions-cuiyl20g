class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_to_index = {}
        result = []
        current_index = 0

        for word in strs:

            word_alpha = [0] * 26
            for letter in word:
                word_alpha[ord(letter) - ord('a')] += 1

            word_alpha = tuple(word_alpha)

            if word_alpha not in word_to_index:

                word_to_index[word_alpha] = current_index
                current_index += 1
                result.append([])

            result[word_to_index[word_alpha]].append(word)

        return result