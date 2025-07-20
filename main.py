def main():
    terrain = Terrain(5, 5)
    manager = RobotManager(terrain)

    while True:
        print("\n🔧 Options: create, move, location, path, remove, check, all, exit")
        choice = input("Enter command: ").strip().lower()

        if choice == "create":
            try:
                rid = int(input("Enter robot ID (numeric): "))
                manager.create_robot(rid)
            except ValueError:
                print("❌ Invalid ID. Please enter a number.")

        elif choice == "move":
            try:
                rid = int(input("Enter robot ID: "))
                cmd = input("Enter movement (e.g. N3, E2): ").strip().upper()
                manager.move_robot(rid, cmd)
                manager.get_robot_location(rid)
                manager.get_robot_path(rid)
            except ValueError:
                print("❌ Invalid input. Robot ID must be a number.")

        elif choice == "location":
            try:
                rid = int(input("Enter robot ID: "))
                manager.get_robot_location(rid)
            except ValueError:
                print("❌ Invalid input. Robot ID must be a number.")

        elif choice == "path":
            try:
                rid = int(input("Enter robot ID: "))
                manager.get_robot_path(rid)
            except ValueError:
                print("❌ Invalid input. Robot ID must be a number.")

        elif choice == "remove":
            try:
                rid = int(input("Enter robot ID to remove: "))
                terrain.remove_robot(rid)
                if rid in manager.robots:
                    del manager.robots[rid]
                print(f"🗑️ Robot {rid} removed from terrain.")
            except ValueError:
                print("❌ Invalid input. Robot ID must be a number.")

        elif choice == "check":
            try:
                r = int(input("Enter row: "))
                c = int(input("Enter column: "))
                print(f"Is ({r},{c}) occupied? {terrain.is_occupied(r, c)}")
            except ValueError:
                print("❌ Invalid input. Please enter numeric row and column.")

        elif choice == "all":
            print("🤖 All robot positions:")
            for rid, pos in terrain.occupied_positions.items():
                print(f"Robot {rid} is at: {pos}")
            print(terrain)

        elif choice == "exit":
            print("🚪 Exiting program. Goodbye!")
            break

        else:
            print("❓ Invalid option.")

main()
