from dataloader import DataLoader
from task1 import Task1

class Main():
    """
    Main
    """
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_loader.load('data/input.txt')
        self.data = self.data_loader.get()
        
        self.task1 = Task1(self.data)
        self.run_task(self.task1)
        

    def run_task(self, task:Task1):
        """
        Run
        """
        print('Task 1 - Sum of all numbers in the file:')
        task.solve()
        print(f"\t{task.get_result()}")

if __name__ == '__main__':
    Main()