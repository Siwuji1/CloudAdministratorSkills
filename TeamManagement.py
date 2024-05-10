# TeamManagement.py

class TeamManager:
    def __init__(self, team_name, team_members):
        self.team_name = team_name
        self.team_members = team_members

    def introduce_team(self):
        print(f"Welcome to Team {self.team_name}!")
        print("Team Members:")
        for member in self.team_members:
            print(f"- {member}")

    def solve_problem(self):
        print("Solving a problem together...")
        # Insert problem-solving logic here

if __name__ == "__main__":
    # Example usage
    team_members = ["Alice", "Bob", "Charlie", "David"]
    manager = TeamManager("CloudOps", team_members)
    manager.introduce_team()
    manager.solve_problem()
