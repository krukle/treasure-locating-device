from task import Task

class Task1(Task):
    """
    Task 1
    """
    def __init__(self, data:list):
        super().__init__(data)
        self.name = 'Task 1'
        self.description = 'Sum of all numbers in the file'

    def solve(self):
        """
        Solve the task    
        """
        self.result = sum(self.data)
        