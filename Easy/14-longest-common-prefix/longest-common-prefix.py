class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

    # Start by assuming the whole first string is the prefix
        prefix = strs[0]

        for word in strs[1:]:
            # Reduce the prefix until it matches the beginning of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Reduce the prefix by one character
                if not prefix:
                    return ""
                    
        return prefix