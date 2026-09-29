class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))
        cars.sort()

        stack = []

        for pos, spd in cars:
            stack.append(float((target - pos) / spd))
        
        fleet = 1
        previous_time = 0

        if stack:
            previous_time = stack.pop()
        else:
            return 0

        while stack:
            time = stack.pop()
            if time > previous_time:
                fleet += 1
                previous_time = time
        
        return fleet