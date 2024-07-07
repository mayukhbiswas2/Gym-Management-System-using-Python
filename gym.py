class Member:
    def __init__(self, member_id, name, age, weight, height, dob, doj, membership_type):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.dob = dob
        self.doj = doj
        self.membership_type = membership_type

class Trainer:
    def __init__(self, trainer_id, name, age, speciality, experience):
        self.trainer_id = trainer_id
        self.name = name
        self.age = age
        self.speciality = speciality
        self.experience = experience

class Session:
    def __init__(self, session_period, trainer_assigned, session_type):
        self.session_period = session_period
        self.trainer_assigned = trainer_assigned
        self.session_type = session_type

class GymManagementSystem:
    print("Welcome to DM Fitness")
    def __init__(self):
        self.members = []
        self.trainers = []
        self.sessions = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} added successfully.")

    def add_trainer(self, trainer):
        self.trainers.append(trainer)
        print(f"Trainer {trainer.name} assigned successfully.")

    def add_session(self, session):
        self.sessions.append(session)
        print(f"Session {session.name} added successfully.")

    def view_members(self):
        for member in self.members:
            print(f"ID: {member.member_id}, Name: {member.name}, Age: {member.age}, Weight: {member.weight}, Height: {member.height} , Date of Birth: {member.dob}, Date of Joining: {member.doj}, Membership: {member.membership_type}")

    def view_trainers(self):
        for trainer in self.trainers:
            print(f"Name: {trainer.name}, Age: {trainer.age}, ID: {trainer.trainer_id}, Specialization: {trainer.speciality}, Experience: {trainer.experience}")

    def view_sessions(self):
        for session in self.sessions:
            print(f"Session Period: {session.session_period}, Trainer Assigned: {session.trainer_assigned.name}, Type: {session.session_type}")

    def find_member_by_id(self, member_id):
        return next(
            (member for member in self.members if member.member_id == member_id),
            None,
        )
            
    def find_trainer_by_id(self, trainer_id):
        return next(
            (
                trainer
                for trainer in self.trainers
                if trainer.trainer_id == trainer_id
            ),
            None,
        )

def main():
    gym_system = GymManagementSystem()

    while True:
        print("\nGym Management System")
        print("1. Add Member")
        print("2. Add Trainer")
        print("3. Add Session")
        print("4. View Members")
        print("5. View Trainers")
        print("6. View Sessions")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            member_id = input("Enter member ID: ")
            name = input("Enter name: ")
            age = int(input("Enter your age: "))
            weight = float(input("Enter your weight: "))
            height = float(input("Enter your height: "))
            dob = input("Date of Birth: ")
            doj = input("Date of joining: ")
            membership_type = input("Enter your membership type: ")
            member = Member(member_id, name, age, weight, height, dob, doj, membership_type)
            gym_system.add_member(member)

        elif choice == '2':
            trainer_id = input("Enter trainer ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            speciality = input("Enter speciality: ")
            experience = int(input("Enter experience (years): "))
            trainer = Trainer(trainer_id, name, age, speciality, experience)
            gym_system.add_trainer(trainer)

        elif choice == '3':
            session_period = input("Session Period: ")
            session_type = input("Enter session type: ")
            trainer_id = input("Enter your trainer ID: ")
            if trainer := gym_system.find_trainer_by_id(trainer_id):
                session = Session(session_period, trainer, session_type)
                gym_system.add_session(session)
            else:
                print("Invalid trainer ID.")

        elif choice == '4':
            gym_system.view_members()

        elif choice == '5':
            gym_system.view_trainers()

        elif choice == '6':
            gym_system.view_sessions()

        elif choice == '7':
            print("Exit From The System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
