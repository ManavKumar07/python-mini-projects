# LOG FILE ANALYZER
import os


class LogAnalyzer:

    def __init__(self):
        self.log_file = "sample.log"
        self.report_file = "report.txt"

    # ---------------- Read Log File ----------------

    def read_logs(self):

        if not os.path.exists(self.log_file):
            print("Log file not found.")
            return []

        with open(self.log_file, "r") as file:
            return file.readlines()

    # ---------------- Analyze ----------------

    def analyze_logs(self):

        logs = self.read_logs()

        if not logs:
            return

        total = len(logs)
        info = 0
        warning = 0
        error = 0

        error_messages = []

        for line in logs:

            if "INFO" in line:
                info += 1

            elif "WARNING" in line:
                warning += 1

            elif "ERROR" in line:
                error += 1
                error_messages.append(line.strip())

        print("\n===== LOG REPORT =====")

        print("Total Logs :", total)
        print("INFO :", info)
        print("WARNING :", warning)
        print("ERROR :", error)

        print("\n----- Error Messages -----")

        if error_messages:
            for msg in error_messages:
                print(msg)
        else:
            print("No Errors Found.")

        self.save_report(total, info, warning, error)

    # ---------------- Save Report ----------------

    def save_report(self, total, info, warning, error):

        with open(self.report_file, "w") as file:

            file.write("===== LOG ANALYSIS REPORT =====\n\n")

            file.write(f"Total Logs : {total}\n")
            file.write(f"INFO : {info}\n")
            file.write(f"WARNING : {warning}\n")
            file.write(f"ERROR : {error}\n")

        print("\nReport Saved Successfully.")

    # ---------------- View Log File ----------------

    def display_logs(self):

        logs = self.read_logs()

        if logs:

            print("\n===== LOG FILE =====\n")

            for line in logs:
                print(line.strip())


# ---------------- Main Program ----------------

analyzer = LogAnalyzer()

while True:

    print("\n====== LOG FILE ANALYZER ======")

    print("1. Display Log File")
    print("2. Analyze Log File")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        analyzer.display_logs()

    elif choice == "2":
        analyzer.analyze_logs()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")