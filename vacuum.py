class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)

    def clean(self):
        rows = len(self.environment)
        cols = len(self.environment[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for col in range(left, right + 1):
                self.position = (top, col)
                print(f"Moving to position: {self.position}")
                self.clean_spot(top, col)
            top += 1

            # Traverse from top to bottom
            for row in range(top, bottom + 1):
                self.position = (row, right)
                print(f"Moving to position: {self.position}")
                self.clean_spot(row, right)
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    self.position = (bottom, col)
                    print(f"Moving to position: {self.position}")
                    self.clean_spot(bottom, col)
                bottom -= 1

            # Traverse from bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    self.position = (row, left)
                    print(f"Moving to position: {self.position}")
                    self.clean_spot(row, left)
                left += 1

        print("Cleaning complete. Environment is clean now!")
        self.display_environment()

    def clean_spot(self, row, col):
        if self.environment[row][col] == 1:
            print("Dirty spot found. Cleaning...")
            self.environment[row][col] = 0
            print("Spot cleaned.")
        else:
            print("Spot is already clean.")

    def display_environment(self):
        
        print("\nCurrent state of the environment:")
        for row in self.environment:
            print(row)


def get_environment_input():
    rows = int(input("Enter the number of rows in the environment: "))
    cols = int(input("Enter the number of columns in the environment: "))
    environment = []
    for i in range(rows):
        row = list(map(int, input(f"Enter the values for row {i + 1} (space-separated, 0 = clean, 1 = dirty): ").split()))
        environment.append(row)
    return environment


# Main Program
environment = get_environment_input()
vacuum = VacuumCleanerAgent(environment)
vacuum.clean()
