class Terrain:
    """
    Represents a grid-based terrain where robots can move.
    Each cell in the grid can be occupied by only one robot at a time.
    """
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.occupied_positions = {}  # Maps robot_id -> (row, col)

    def is_within_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_occupied(self, row: int, col: int) -> bool:
        return (row, col) in self.occupied_positions.values()

    def update_position(self, robot_id: int, row: int, col: int):
        self.occupied_positions[robot_id] = (row, col)

    def get_robot_position(self, robot_id: int):
        return self.occupied_positions.get(robot_id, None)

    def remove_robot(self, robot_id: int):
        if robot_id in self.occupied_positions:
            del self.occupied_positions[robot_id]

    def __str__(self):
        return f"Occupied Cells: {self.occupied_positions}"
