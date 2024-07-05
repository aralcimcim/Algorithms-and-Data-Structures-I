class RabinKarp:

    def __init__(self):
        pass

    """
        This method uses the RabinKarp algorithm to search a given pattern in a given input text.
        @ param pattern - The string pattern that is searched in the text.
        @ param text - The text string in which the pattern is searched.
        @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
        @ raises ValueError if pattern or text is None or empty.
    """

    def search(self, pattern, text):
        # TODO
        if not pattern or not text:
            raise ValueError('Either pattern or text is None or empty.')

        pattern_length = len(pattern)
        text_length = len(text)
        pattern_hash = self.get_rolling_hash_value(pattern, None, None)
        text_hash = self.get_rolling_hash_value(text[:pattern_length], None, None)

        print(f"Initial pattern hash: {pattern_hash}")
        print(f"Initial text hash: {text_hash}")

        occurrences = []
        for i in range(1, text_length-pattern_length+2):
            print(f"\nIteration {i}:")
            print(f"Current text hash: {text_hash}")
            if pattern_hash == text_hash:
                print(f"Pattern hash matches text hash")
                if pattern == text[i-1:i + pattern_length-1]:
                    print(f"Pattern found at index {i-1}")
                    occurrences.append(i-1)
            if i < text_length - pattern_length+1:
                text_hash = self.get_rolling_hash_value(text[i:i+pattern_length], text[i-1], text_hash)
                print(f"Text hash updated to {text_hash} for next iteration")

        return occurrences

    """
         This method calculates the (rolling) hash code for a given character sequence. For the calculation use the 
         base b=29.
         @ param sequence - The char sequence for which the (rolling) hash shall be computed.
         @ param last_character - The character to be removed from the hash when a new character is added.
         @ param previous_hash - The most recent hash value to be reused in the new hash value.
         @ return hash value for the given character sequence using base 29.
    """

    @staticmethod
    def get_rolling_hash_value(sequence, last_character, previous_hash):
        # TODO
        base = 29
        hash_val = ((base ** (len(sequence)-1)) * ord(sequence[0])) + ((base ** (len(sequence)-2)) * ord(sequence[-1]))
        
        return hash_val

