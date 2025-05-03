class Solution(object):
    def countSeniors(self, details):
        count = 0
        for passenger in details:
            age = int(passenger[11:13])
            if age > 60:
                count += 1
        return count
        
