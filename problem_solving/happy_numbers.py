class Solution:
    happy = set({1, 10, 13, 31, 68, 86, 100})

    def isHappy(self, n: int):
        potentialHappy = set()
        potentialHappy.add(n)
        seen = set()

        while n not in seen:
            if n in self.happy:
                foundHappy = True
                break
            seen.add(n)
            sum = 0
            while n > 0:
                sum += (n%10) ** 2
                n //=10
            potentialHappy.add(sum)
            if sum == 1:
                foundHappy = True
                break
            n = sum

        if foundHappy:
            
            self.happy |= potentialHappy
            return True

        return False

    def happyInRange(self, start, end: int):
        # Reverse numbers and check if already found to be happy
        pass

    def getAllHappyNumbers(self):
        return self.happy

s = Solution()
s.isHappy(19)
s.isHappy(20)
# happyNumbers = s.happyInRange(5, 20)
print(s.getAllHappyNumbers())
