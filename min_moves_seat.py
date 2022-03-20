def minMovesToSeat( seats, students) -> int:
        seats.sort()
        students.sort()
        count_moves = 0
        for i in range(len(seats)):
            count_moves += abs(students[i] - seats[i])
        return count_moves
       

seats = [3,1,5]
students = [2,7,4]
print(minMovesToSeat(seats,students))
