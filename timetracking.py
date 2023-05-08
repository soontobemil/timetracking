import os
import json
import glob

def print_vega_ascii_art():
    vega_ascii_art = r"""
                                                                                
 __     __ U _____ u   ____      _      
 \ \   /"/u\| ___"|/U /"___|uU  /"\  u  
  \ \ / //  |  _|"  \| |  _ / \/ _ \/   
  /\ V /_,-.| |___   | |_| |  / ___ \   
 U  \_/-(_/ |_____|   \____| /_/   \_\  
   //       <<   >>   _)(|_   \\    >>  ;
  (__)     (__) (__) (__)__) (__)  (__)
"""
    print(vega_ascii_art)

def save_time_tracking_data(date, data):
    filename = f"{date}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_data = json.load(file)
        for key, value in data.items():
            if key in existing_data:
                existing_data[key] += value
            else:
                existing_data[key] = value
        data = existing_data

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def input_str_no_numbers(prompt):
    while True:
        value = input(prompt)
        if not any(char.isdigit() for char in value):
            return value
        print("Please enter a string without numbers.")

def choose_file():
    files = glob.glob("*.txt")
    if files:
        print("\nChoose a file to update:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        print(f"{len(files) + 1}. Create a new file")
        choice = input_int("Enter the number of the chosen file: ")
        if 1 <= choice <= len(files):
            return files[choice - 1].replace(".txt", "")
        elif choice == len(files) + 1:
            return input("\nEnter today's date (YYYY-MM-DD): ")
        else:
            print("Invalid choice. Please try again.")
            return choose_file()
    else:
        return input("\nEnter today's date (YYYY-MM-DD): ")

def main():
    print_vega_ascii_art()
    print("\nWelcome to VEGA TimeTracking!")

    date = choose_file()

    time_spent = {}

    categories = [
        "Non-technical team-work",
        "Backlog",
        "Off-Team",
        "Fastlane"
    ]

    while True:
        print("\nChoose a category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        print(f"{len(categories) + 1}. Exit")

        choice = input_int("Enter the number of the chosen category: ")
        if choice == len(categories) + 1:
            break
        if 1 <= choice <= len(categories):
            category = categories[choice - 1]
            time_minutes = input_int(f"\nTime spent on {category} (in minutes): ")
            work_type = input_str_no_numbers("What kind of work did you do? ")
            key = f"{category}: {work_type}"
            time_spent[key] = time_minutes
        else:
            print("Invalid choice. Please try again.")

    save_time_tracking_data(date, time_spent)

if __name__ == "__main__":
    main()
