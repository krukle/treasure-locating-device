from task import Task

class Task1(Task):
    """
    Task 1

    Sum of all numbers in the file
    
    Args:
        data (list): data
    
    Attributes:
        data (list): data
        result (int): result
        name (str): name
        description (str): description
    """
    def __init__(self, data:list):
        """
        Initialize the task

        Args:
            data (list): data
        """
        super().__init__(data)
        self.name = 'Task 1'
        self.description = 'Sum of all numbers in the file'

    def solve(self):
        """
        Solve the task  
        
        Sum of all numbers in the file
        """
        self.result = sum(self.data)
        