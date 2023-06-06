class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}
        for letter in chars:
            char_count[letter] = char_count.get(letter, 0) + 1
        
        result = 0
        for word in words:
            new_word_chars = {}
            for letter in word:
                new_word_chars[letter] = new_word_chars.get(letter, 0) + 1
            
            good_word_flag = True
            for char, count in new_word_chars.items():
                if char not in char_count or count > char_count[char]:
                    good_word_flag = False
            
            if good_word_flag:
                result += len(word)
        
        return result