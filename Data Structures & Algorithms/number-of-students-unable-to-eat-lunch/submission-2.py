from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # -- OPTIMAL SOLUTION ---
        # ones = students.count(1)
        # zeroes = students.count(0)


        # for i in sandwiches:
        #     if i == 0:
        #         if zeroes == 0:
        #             return ones
        #         zeroes -= 1
        #     else:
        #         if ones == 0:
        #             return zeroes
        #         ones -= 1
        
        # return 0

        #-- Queue solution --
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0
        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:
                students.append(students.popleft())
                count += 1
            if count == len(students):
                return len(students)
        return 0
                
                
            


        



        