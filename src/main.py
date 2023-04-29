from dataloader import DataLoader
from task1 import Task1
from task2 import Task2

class Main():
    """
    Main
    """
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_loader.load('data/input.txt')
        self.data = self.data_loader.get()
        self.tasks = [Task1(self.data), Task2(self.data)]
        for task in self.tasks:
            self.run_task(task)

    def run_task(self, task:Task1):
        """
        Run
        """
        print (f'Running {task.get_name()} - {task.get_description()}...')
        task.solve()
        print(f"Result: {task.get_result()}")

if __name__ == '__main__':
    Main()