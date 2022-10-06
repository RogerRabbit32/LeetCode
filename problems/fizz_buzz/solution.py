class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x = []
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                x.append(str(i))
            elif i % 3 == 0 and i % 5 != 0:
                x.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                x.append('Buzz')
            else:
                x.append('FizzBuzz')
        return x
