class Robot:
    """
    Represents a robot that can move on the terrain.
    Supports cardinal and diagonal directions.
    """

    DIRECTION_MAP = {
        'N': (-1, 0),   # Up
        'S': (1, 0),    # Down
        'E': (0, 1),    # Right
        'W': (0, -1),   # Left
        'NE': (-1, 1),  # Up-Right
        'NW': (-1, -1), # Up-Left
        'SE': (1, 1),   # Down-Right
        'SW': (1, -1),  # Down-Left
    }

    def __init__(self, robot_id: int):
        self.robot_id = robot_id
        self.position = (0, 0)
        self.path_history = [self.position]

    def get_position(self):
        return self.position

    def get_path_history(self):
        return self.path_history

    def move(self, direction: str, steps: int, terrain):
        if direction not in self.DIRECTION_MAP:
            print(f"❌ Invalid direction '{direction}' for Robot {self.robot_id}.")
            return

        dr, dc = self.DIRECTION_MAP[direction]
        row, col = self.position

        for _ in range(steps):
            new_row = row + dr
            new_col = col + dc

            # Bounds check with edge reason
            if not terrain.is_within_bounds(new_row, new_col):
                boundary_reason = ""
                if new_row < 0: boundary_reason += "top "
                elif new_row >= terrain.rows: boundary_reason += "bottom "
                if new_col < 0: boundary_reason += "left"
                elif new_col >= terrain.cols: boundary_reason += "right"

                print(f"⚠️ Robot {self.robot_id} is at {self.position} and cannot move {direction} — it’s at the {boundary_reason.strip()} edge.")
                break

            if terrain.is_occupied(new_row, new_col):
                print(f"⚠️ Robot {self.robot_id} stopped before collision at ({row}, {col})")
                break

            row, col = new_row, new_col
            self.path_history.append((row, col))

        self.position = (row, col)
        terrain.update_position(self.robot_id, row, col)
        print(f"✅ Robot {self.robot_id} moved to {self.position}")
