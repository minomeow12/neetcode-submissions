class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        

        ones = students.count(1)
        zeroes = students.count(0)


        for i in sandwiches:
            if i == 0:
                if zeroes == 0:
                    return ones
                zeroes -= 1
            else:
                if ones == 0:
                    return zeroes
                ones -= 1
        if zeroes == 0 and ones == 0:
                return 0
                
                
            


        



        