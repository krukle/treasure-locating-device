
class DataLoader:
    def __init__(self):
        self.data = []

    def load(self, file:str):
        """
        Load data from file

        Args:
            file (str): path to file
        """
        with open (file, 'r') as f:
            self.data = [int(line.strip()) for line in f.readlines()]
    
    def get(self) -> list:
        """
        Get data
        
        Returns:
            list: data
        """
        return self.data