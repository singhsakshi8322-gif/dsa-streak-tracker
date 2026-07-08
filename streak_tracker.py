"""
DSA Streak Tracker
-------------------
A simple command-line tool to log your daily DSA practice,
track your streak, and stay motivated with consistency stats.

No external libraries needed — pure Python standard library.
"""

import json
import os
from datetime import date, timedelta

DATA_FILE = "streak_data.json"


# ---------- Data handling ----------

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"logs": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ---------- Core features ----------

def log_today(data):
    today = str(date.today())
    if today in data["logs"]:
        print(f"\n✅ You already logged today ({today}). No changes made.\n")
        return

    problem_name = input("What problem did you solve today? ").strip()
    difficulty = input("Difficulty (easy/medium/hard): ").strip().lower()
    platform = input("Platform (leetcode/codeforces/other): ").strip().lower()

    data["logs"][today] = {
        "problem": problem_name or "Unnamed problem",
        "difficulty": difficulty if difficulty in ("easy", "medium", "hard") else "unspecified",
        "platform": platform or "unspecified",
    }
    save_data(data)
    print(f"\n🔥 Logged! '{problem_name}' saved for {today}.\n")


def calculate_streak(data):
    if not data["logs"]:
        return 0

    logged_dates = set(data["logs"].keys())
    streak = 0
    current = date.today()

    # If today isn't logged yet, streak counts up to yesterday
    if str(current) not in logged_dates:
        current -= timedelta(days=1)

    while str(current) in logged_dates:
        streak += 1
        current -= timedelta(days=1)

    return streak


def show_stats(data):
    total = len(data["logs"])
    streak = calculate_streak(data)

    difficulty_count = {"easy": 0, "medium": 0, "hard": 0, "unspecified": 0}
    for entry in data["logs"].values():
        difficulty_count[entry.get("difficulty", "unspecified")] += 1

    print("\n" + "=" * 40)
    print("STATS")
    print("=" * 40)
    print(f"  Total problems logged : {total}")
    print(f"  Current streak        : {streak} day(s)")
    print("  Breakdown by difficulty:")
    for level, count in difficulty_count.items():
        if count > 0:
            print(f"    - {level.capitalize():<12}: {count}")
    print("=" * 40)

    if streak == 0:
        print("  No active streak yet — log today's problem to start one!")
    elif streak < 7:
        print("  Nice start — keep it going for a full week!")
    elif streak < 30:
        print("  Solid consistency — you're building a real habit.")
    else:
        print("  Incredible discipline — this is what mastery looks like.")
    print()


def show_history(data):
    if not data["logs"]:
        print("\nNo problems logged yet.\n")
        return

    print("\n" + "-" * 55)
    print("PROBLEM HISTORY (most recent first)")
    print("-" * 55)
    for day in sorted(data["logs"].keys(), reverse=True):
        entry = data["logs"][day]
        print(f"  {day}  |  {entry['problem']:<25} | {entry['difficulty']:<10} | {entry['platform']}")
    print("-" * 55 + "\n")


def show_calendar(data):
    """Shows a simple text calendar of the last 30 days with ticks for logged days."""
    print("\nLAST 30 DAYS\n")
    today = date.today()
    row = ""
    for i in range(29, -1, -1):
        day = today - timedelta(days=i)
        mark = "#" if str(day) in data["logs"] else "."
        row += mark
        if (30 - i) % 10 == 0:
            row += "\n"
    print(row)
    print()


# ---------- Menu ----------

def print_menu():
    print("\n" + "=" * 40)
    print("   DSA STREAK TRACKER")
    print("=" * 40)
    print("  1. Log today's problem")
    print("  2. View stats")
    print("  3. View history")
    print("  4. View 30-day calendar")
    print("  5. Exit")
    print("=" * 40)


def main():
    data = load_data()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            log_today(data)
        elif choice == "2":
            show_stats(data)
        elif choice == "3":
            show_history(data)
        elif choice == "4":
            show_calendar(data)
        elif choice == "5":
            print("\nKeep the streak alive. See you tomorrow!\n")
            break
        else:
            print("\nInvalid option — please choose between 1 and 5.\n")


if __name__ == "__main__":
    main()
