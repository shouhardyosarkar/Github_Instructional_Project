import csv
import os
import datetime
import random
import getpass
import platform

LOG_DIR = "logs"

HEADER = [
    "timestamp_utc",
    "watcher_name",
    "machine_id",
    "cpu_load_pct",
    "temp_celsius",
    "error_rate",
    "notes_this_shift",
    "handoff_to_next"
]

def ensure_log_dir():
    os.makedirs(LOG_DIR, exist_ok=True)

def list_csv_files():
    """Return list of (filename, full_path, mtime)."""
    ensure_log_dir()
    files = []
    for name in os.listdir(LOG_DIR):
        if name.lower().endswith(".csv"):
            full = os.path.join(LOG_DIR, name)
            mtime = os.path.getmtime(full)
            files.append((name, full, mtime))
    # sort by name for display stability
    files.sort()
    return files

def pretty_time(ts):
    """Format timestamp (float seconds since epoch) to readable string."""
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def get_latest_csv():
    """Return (name, full_path) of the most recently modified csv, or None."""
    files = list_csv_files()
    if not files:
        return None
    # pick max by mtime
    latest = max(files, key=lambda row: row[2])
    return latest[0], latest[1]

def show_csv_preview(full_path, max_lines=10):
    """Print first `max_lines` data rows of the CSV for preview."""
    if not os.path.exists(full_path):
        print("[!] File not found.")
        return
    print(f"\n--- Preview of {full_path} ---")
    with open(full_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(row)
            if i >= max_lines:
                print("... (truncated preview)")
                break
    print("--- End preview ---\n")

def create_new_logfile():
    """Create a new CSV with header. Return (name, full_path)."""
    ensure_log_dir()
    # propose default filename based on date
    date_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    default_name = f"{date_str}_shift_log.csv"
    print(f"\nEnter new log filename (default: {default_name}):")
    user_in = input("> ").strip()
    if user_in == "":
        filename = default_name
    else:
        # ensure .csv extension
        if not user_in.lower().endswith(".csv"):
            filename = user_in + ".csv"
        else:
            filename = user_in

    full_path = os.path.join(LOG_DIR, filename)
    if os.path.exists(full_path):
        print(f"[!] {filename} already exists, will NOT overwrite.")
        return None, None

    with open(full_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)

    print(f"[OK] Created new log file: {full_path}")
    return filename, full_path

def collect_machine_id():
    """Machine/environment signature to make each entry identifiable."""
    os_name = platform.system()
    os_ver = platform.release()
    user = getpass.getuser()
    return f"{os_name}-{os_ver}-{user}"

def simulate_metrics():
    """Fake monitoring data for demo."""
    cpu_load = round(random.uniform(5, 85), 1)          # pretend CPU usage %
    temp = round(random.uniform(30.0, 75.0), 1)         # pretend sensor temp (C)
    error_rate = round(random.uniform(0.0, 2.0), 3)     # pretend error %
    return cpu_load, temp, error_rate

def append_shift_entry(full_path):
    """Ask user for info and append one row to an existing CSV."""
    if not os.path.exists(full_path):
        print("[!] That file doesn't exist.")
        return

    print("\n=== Log new shift entry ===")
    watcher_name = input("Your name (e.g. Alice): ").strip()

    cpu_load, temp_c, err_rate = simulate_metrics()
    print(f"\n[Simulated metrics this shift]")
    print(f"  CPU load %      : {cpu_load}")
    print(f"  Temp (C)        : {temp_c}")
    print(f"  Error rate (%)  : {err_rate}")

    print("\nNotes for this shift (what happened / what you observed):")
    notes = input("> ").strip()

    print("\nHandoff message for next shift (what they should watch next):")
    handoff = input("> ").strip()

    ts = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    machine_id = collect_machine_id()

    row = [
        ts,
        watcher_name,
        machine_id,
        cpu_load,
        temp_c,
        err_rate,
        notes,
        handoff
    ]

    with open(full_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("\n[OK] New shift entry appended.")
    print(f"File updated: {full_path}")
    print("Reminder: git add logs && git commit && git push\n")

def choose_file_interactively():
    """Let the user pick a CSV file from the list."""
    files = list_csv_files()
    if not files:
        print("[!] No CSV logs found.")
        return None, None

    print("\nAvailable log files:")
    for idx, (name, full, mtime) in enumerate(files, start=1):
        print(f"  {idx}. {name}   (last modified {pretty_time(mtime)})")

    print("Select a file by number:")
    try:
        choice = int(input("> ").strip())
    except ValueError:
        print("[!] Invalid input.")
        return None, None

    if choice < 1 or choice > len(files):
        print("[!] Out of range.")
        return None, None

    return files[choice-1][0], files[choice-1][1]

def main_menu():
    ensure_log_dir()
    while True:
        print("\n========================")
        print(" Shift Log Control Menu ")
        print("========================")
        print("1) List all log CSV files")
        print("2) Show preview of a log file")
        print("3) Show most recently edited log file")
        print("4) Append new shift entry to an existing log file")
        print("5) Create a new log file and start logging")
        print("6) Quit")
        choice = input("> ").strip()

        if choice == "1":
            files = list_csv_files()
            if not files:
                print("\n(No log files yet.)\n")
            else:
                print("\nLog files:")
                for name, full, mtime in files:
                    print(f" - {name}  (last modified {pretty_time(mtime)})")
                print("")

        elif choice == "2":
            _, full_path = choose_file_interactively()
            if full_path:
                show_csv_preview(full_path)

        elif choice == "3":
            latest = get_latest_csv()
            if not latest:
                print("\n(No log files yet.)\n")
            else:
                name, full = latest
                print(f"\nMost recent log file: {name}")
                show_csv_preview(full)

        elif choice == "4":
            name, full_path = choose_file_interactively()
            if full_path:
                append_shift_entry(full_path)

        elif choice == "5":
            name, full_path = create_new_logfile()
            if full_path:
                # immediately log first shift into it
                append_shift_entry(full_path)

        elif choice == "6":
            print("Exiting. Remember to git add/commit/push your updated logs/")
            break

        else:
            print("[!] Invalid selection, please choose 1-6.")

if __name__ == "__main__":
    main_menu()
