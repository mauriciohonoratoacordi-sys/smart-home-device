"""
Smart Home Device Manager
--------------------------
A simple console program for Bright Minds Academy to keep track of
smart classroom devices (name, location and connectivity status).

Data structure used:
    devices = [
        {"name": "Smart Light A1", "location": "Room 101", "status": "online"},
        {"name": "Projector B2",   "location": "Room 204", "status": "offline"},
        ...
    ]

Each device is a dictionary and all devices are stored together in a
list. A list of dictionaries was chosen because:
    - it keeps every device's data (name, location, status) grouped together
    - it is easy to loop through when viewing or searching devices
    - it does not require a database, which matches the task requirements
"""

# Allowed status values. Using a constant list means the validation
# rule only needs to be written once and can be reused everywhere.
VALID_STATUSES = ["online", "offline", "under maintenance"]


def add_device(devices):
    """
    Ask the user for a device name and location, then add the new
    device to the devices list with a default status of 'offline'.
    Includes validation so empty names/locations and duplicate
    device names are rejected.
    """
    print("\n--- Add New Device ---")

    # Validate the device name: it must not be empty and must not
    # already exist in the list (case-insensitive check).
    while True:
        name = input("Enter device name (e.g. Smart Light A1): ").strip()
        if name == "":
            print("Device name cannot be empty. Please try again.")
            continue
        if any(device["name"].lower() == name.lower() for device in devices):
            print(f"A device named '{name}' already exists. Please use a different name.")
            continue
        break

    # Validate the location: it must not be empty.
    while True:
        location = input("Enter device location (e.g. Room 101): ").strip()
        if location == "":
            print("Location cannot be empty. Please try again.")
            continue
        break

    # New devices start as 'offline' until the staff update them.
    new_device = {"name": name, "location": location, "status": "offline"}
    devices.append(new_device)
    print(f"Device '{name}' added successfully in {location} (status: offline).")


def update_device_status(devices):
    """
    Ask the user for a device name and a new status, then update
    that device's status in the list. Validates that the device
    exists and that the status entered is one of the allowed values.
    """
    print("\n--- Update Device Status ---")

    if not devices:
        print("There are no devices to update yet. Please add a device first.")
        return

    name = input("Enter the name of the device to update: ").strip()

    # Search for the device first (linear search through the list).
    device_found = None
    for device in devices:
        if device["name"].lower() == name.lower():
            device_found = device
            break

    if device_found is None:
        print(f"No device named '{name}' was found.")
        return

    # Validate the new status against the allowed list.
    while True:
        print(f"Valid statuses: {', '.join(VALID_STATUSES)}")
        new_status = input("Enter new status: ").strip().lower()
        if new_status not in VALID_STATUSES:
            print("Invalid status entered. Please choose one of the valid statuses shown above.")
            continue
        break

    device_found["status"] = new_status
    print(f"Device '{device_found['name']}' status updated to '{new_status}'.")


def view_devices(devices):
    """
    Display every device currently stored, along with its location
    and status, in a simple table format.
    """
    print("\n--- Device List ---")

    if not devices:
        print("No devices have been added yet.")
        return

    # Simple formatted table using string formatting for alignment.
    print(f"{'Name':<20}{'Location':<15}{'Status':<20}")
    print("-" * 55)
    for device in devices:
        print(f"{device['name']:<20}{device['location']:<15}{device['status']:<20}")


def search_device(devices):
    """
    Ask the user for a device name and display its status and
    location if found. Handles the case where the device does not
    exist and where the search term is left empty.
    """
    print("\n--- Search for a Device ---")

    if not devices:
        print("There are no devices to search yet. Please add a device first.")
        return

    name = input("Enter the device name to search for: ").strip()
    if name == "":
        print("Search term cannot be empty.")
        return

    for device in devices:
        if device["name"].lower() == name.lower():
            print(f"Name: {device['name']}")
            print(f"Location: {device['location']}")
            print(f"Status: {device['status']}")
            return

    print(f"No device named '{name}' was found.")


def get_menu_choice():
    """
    Display the main menu and validate that the user enters a
    number between 1 and 5.
    """
    print("\n===== Smart Home Device Manager =====")
    print("1. Add new device")
    print("2. Update device status")
    print("3. View device list")
    print("4. Search for a device")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        print("Invalid choice. Please enter a number between 1 and 5.")


def main():
    """
    Main program loop. Keeps showing the menu and calling the
    relevant function until the user chooses to exit.
    """
    devices = []  # This list holds all devices for the duration of the program

    print("Welcome to the Bright Minds Academy Smart Device Manager.")

    while True:
        choice = get_menu_choice()

        if choice == "1":
            add_device(devices)
        elif choice == "2":
            update_device_status(devices)
        elif choice == "3":
            view_devices(devices)
        elif choice == "4":
            search_device(devices)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
