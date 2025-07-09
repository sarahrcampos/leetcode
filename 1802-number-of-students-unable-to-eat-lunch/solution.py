#0 = circular
#1 = square
#len(sandwiches) = len(students)
#sandwiches = stack -> [0] is the top
#students = queue -> [0] is the front

#how to avoid infinite loop?
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = sandwiches[::-1]

        while students:
            for _ in range(len(students)):
                student = students.popleft()
                if student == sandwiches[-1]:
                    sandwiches.pop()
                else:
                    students.append(student)
            if sandwiches and sandwiches[-1] not in students:
                return len(students)
        return 0

        #students = [0,0,0,1,1,1,1,0,0,0] sandwiches = [1,0,1,0,0,1,1,0,0,0]
        #0,0,1,1,1,1,0,0,0,0
        #1,1,1,1,0,0,0,0,0,0
        #1,1,1,0,0,0,0,0,0 | 0,1,0,0,1,1,0,0,0
        #0,0,0,0,0,0,1,1,1
        #0,0,0,0,0,1,1,1 | 1,0,0,1,1,0,0,0
