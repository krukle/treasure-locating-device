from task import Task

class Task2(Task):
    """
    Task 2

    First frequency reached twice

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
        self.name = 'Task 2'
        self.description = 'First frequency reached twice'

    def solve(self):
        """
        Solve the task

        First frequency reached twice
        """
        frequencies = {0}
        current_frequency = 0
        while True:
            for change in self.data:
                current_frequency += change
                if current_frequency in frequencies:
                    self.result = current_frequency
                    return
                frequencies.add(current_frequency)
