class RobotManager:
    def __init__(self, terrain):
        self.terrain = terrain
        self.robots = {}

    def create_robot(self, robot_id: int):
        if robot_id in self.robots:
            print(f"⚠️ Robot {robot_id} already exists.")
            return

        robot = Robot(robot_id)
        self.robots[robot_id] = robot
        self.terrain.update_position(robot_id, 0, 0)
        print(f"✅ Robot {robot_id} created at (0, 0)")

    def move_robot(self, robot_id: int, command: str):
        if robot_id not in self.robots:
            print(f"❌ Robot {robot_id} does not exist.")
            return

        # Extract direction (letters) and steps (digits) from command
        direction = ''
        steps_str = ''
        for char in command:
            if char.isalpha():
                direction += char.upper()
            elif char.isdigit():
                steps_str += char
            else:
                print(f"❌ Invalid character in command: {char}")
                return

        if direction not in Robot.DIRECTION_MAP or not steps_str:
            print(f"❌ Invalid command format: {command}")
            return

        steps = int(steps_str)
        self.robots[robot_id].move(direction, steps, self.terrain)

    def get_robot_location(self, robot_id: int):
        if robot_id in self.robots:
            print(f"📍 Robot {robot_id} is at {self.robots[robot_id].get_position()}")

    def get_robot_path(self, robot_id: int):
        if robot_id in self.robots:
            print(f"📜 Robot {robot_id} path: {self.robots[robot_id].get_path_history()}")
