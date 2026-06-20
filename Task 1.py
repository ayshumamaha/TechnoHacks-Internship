import json
import time
from datetime import datetime

FILE_NAME = "reminders.json"


def load_reminders():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_reminders(reminders):
    with open(FILE_NAME, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(reminders):

    title = input("Enter reminder title: ")

    date = input("Enter date (YYYY-MM-DD): ")

    reminder_time = input("Enter time (HH:MM): ")

    try:
        datetime.strptime(
            date + " " + reminder_time,
            "%Y-%m-%d %H:%M"
        )

    except ValueError:
        print("Invalid date or time format.")
        return

    reminder = {
        "title": title,
        "date": date,
        "time": reminder_time,
        "status": "Pending"
    }

    reminders.append(reminder)

    save_reminders(reminders)

    print("Reminder added successfully.")


def view_reminders(reminders):

    if not reminders:
        print("No reminders available.")
        return

    for index, reminder in enumerate(reminders, start=1):

        print(f"\nReminder {index}")

        print("Title:", reminder["title"])

        print("Date:", reminder["date"])

        print("Time:", reminder["time"])

        print("Status:", reminder["status"])


def delete_reminder(reminders):

    if not reminders:
        print("No reminders available.")
        return

    view_reminders(reminders)

    try:

        choice = int(
            input("Enter reminder number to delete: ")
        )

        reminders.pop(choice - 1)

        save_reminders(reminders)

        print("Reminder deleted successfully.")

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Reminder number does not exist.")


def check_reminders(reminders):

    current = datetime.now()

    for reminder in reminders:

        reminder_datetime = datetime.strptime(
            reminder["date"] + " " + reminder["time"],
            "%Y-%m-%d %H:%M"
        )

        if (
            current >= reminder_datetime
            and reminder["status"] == "Pending"
        ):

            print("\n===================")
            print("REMINDER ALERT")
            print("===================")

            print("Task:", reminder["title"])

            reminder["status"] = "Completed"

            save_reminders(reminders)


def main():

    reminders = load_reminders()

    while True:

        check_reminders(reminders)

        print("\n===== SMART REMINDER =====")

        print("1. Add Reminder")

        print("2. View Reminders")

        print("3. Delete Reminder")

        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            add_reminder(reminders)

        elif choice == "2":

            view_reminders(reminders)

        elif choice == "3":

            delete_reminder(reminders)

        elif choice == "4":

            print("Exiting Application...")
            break

        else:

            print("Invalid choice.")

        time.sleep(1)


main()


