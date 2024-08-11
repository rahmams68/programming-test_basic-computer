class QuestionOneSolution:    
    def twoSum(self, nums: list[int], target: int):
        # Dictionary of already evaluated numbers
        prevNum = {}
        
        for index, num in enumerate(nums):
            # Looking for pair (the difference between num and target)
            diff = target - num

            if diff in prevNum:
                # print(f'{num} + {diff} = {target}')
                return [index, prevNum[diff]]
            
            prevNum[num] = index
    
    def test(self):
        print(self.twoSum([2, 7, 11, 15], 9))
        print(self.twoSum([2, 7, 11, 15], 13))
    
solution = QuestionOneSolution()
solution.test()