
class Task1():
    """
    Task 1
    
    Attributes:
        dataLoader (DataLoader): data loader
        data (list): data
        result (int): result
    """
    def __init__(self, data:list):
        self.data = data
        self.result = 0

    def solve(self):
        """
        Solve the task    
        """
        self.result = sum(self.data)

    def get_result(self) -> int:
        """
        Get result

        Returns:
            int: result
        """
        return self.result