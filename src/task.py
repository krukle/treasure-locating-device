
class Task():
    """
    Create a new class Task that Task1 and Task2 inherit from.

    Args:
        data (list): data

    Attributes:
        data (list): data
        result (int): result
        name (str): name
        description (str): description
    """
    def __init__(self, data:list):
        self.data = data
        self.result = 0
        self.name = 'Task'
        self.description = 'Description'
    
    def get_name(self) -> str:
        """
        Get name

        Returns:
            str: name
        """
        return self.name

    def get_description(self) -> str:
        """
        Get description

        Returns:
            str: description
        """
        return self.description

    def solve(self):
        """
        Solve the task
        """
        pass

    def get_result(self) -> int:
        """
        Get result

        Returns:
            int: result
        """
        return self.result
