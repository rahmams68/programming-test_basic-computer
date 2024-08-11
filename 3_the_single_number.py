class QuestionThreeSolution:    
    def singleNumber(self, nums: list[int]):
        prevNum = {}
        single_number = None
        
        for num in nums:
            if num in prevNum:
                prevNum[num] += 1
            else:
                prevNum[num] = 1
        
        for num, count in prevNum.items():
            if count == 1:
                single_number = num
        
        print(f'In {nums}, the single number is: {single_number}')
        
        return single_number
    
    def test(self):
        self.singleNumber([1, 1, 3, 4, 5, 4, 5])
        self.singleNumber([9, 0, 9, 8, 8, 7, 0])
    
solution = QuestionThreeSolution()
solution.test()