"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Tests for equality based on student names."""
        return self.name == other.name

    def __lt__(self, other):
        """Tests for less than based on student names."""
        return self.name < other.name

    def __ge__(self, other):
        """Tests for greater than or equal to based on student names."""
        return self.name >= other.name
        
def main():
    s1 = Student("Robbie", 1)
    s2 = Student("King", 1)
    s1.setScore(1, 70)
    s2.setScore(1, 69)
    print("Student 1:\n", s1 , "\n")
    print("Student 2:\n", s2 , "\n")
    print(s1 , " equal to " , s2 , " ?: ", s1.__eq__(s2) , "\n")
    print(s1 , " less than " , s2 , " ?: ", s1.__lt__(s2) , "\n")
    print(s1 , " greater than " , s2 , " ?: ", s1.__ge__(s2) , "\n")
    print(s2 , " equal to " , s1 , " ?: ", s2.__eq__(s1) , "\n")
    print(s2 , " less than " , s1 , " ?: ", s2.__lt__(s1) , "\n")
    print(s2 , " greater than " , s1, " ?: ", s2.__ge__(s1) , "\n")

if __name__ == "__main__":
    main()