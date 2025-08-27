class Solution:
    #monotonic increasing stack
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position,speed)]
        cars.sort(reverse=True)

        stack = []
        for position, speed in cars:
            time = (target - position)/speed
            if stack and time <= stack[-1] :
                time = stack.pop()
            stack.append(time)

        return len(stack)
