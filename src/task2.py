from task import Task

class Task2(Task):

    def __init__(self, data:list):
        super().__init__(data)
        self.name = 'Task 2'
        self.description = 'First frequency reached twice'

    def solve(self):
        """
        Solve the task
        """
        frequencies = [0]
        current_frequency = 0
        while True:
            for change in self.data:
                current_frequency += change
                if current_frequency in frequencies:
                    self.result = current_frequency
                    return
                frequencies.append(current_frequency)
