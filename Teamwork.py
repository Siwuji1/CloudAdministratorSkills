# Teamwork.py

class Teamwork:
    def __init__(self, team_name, team_members):
        self.team_name = team_name
        self.team_members = team_members

    def introduce_team(self):
        print(f"Welcome to Team {self.team_name}!")
        print("Team Members:")
        for member in self.team_members:
            print(f"- {member}")

if __name__ == "__main__":
    team_members = ["Alice", "Bob", "Charlie", "David"]
    team = Teamwork("CloudOps", team_members)
    team.introduce_team()
