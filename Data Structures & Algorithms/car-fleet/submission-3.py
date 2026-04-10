class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([[p,s] for p, s in zip(position,speed)], reverse= True)
        stack = []
        for c in pairs:
            time = (target - c[0])/c[1]
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
    

        