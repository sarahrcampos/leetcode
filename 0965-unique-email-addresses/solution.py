class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        map = {}
        for email in emails:
            splitted = email.split('@')
            splitted[0] = splitted[0].split('+')[0].replace('.', '')
            actual = "@".join(splitted)
            if actual not in map:
                map[actual] = True
        return len(map)

        
