# Entry script that should call the reporting logic from lib/report_generator.py
import csv
from datetime import datetime

# TODO: Import your report generator module
# from lib.report_generator import generate_csv_report

def main():
    # TODO: Call generate_csv_report()
    # This script will be run using `python generate_report.py`
    # Generate report
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Status"])
        writer.writerow([1, "Complete"])
    print(f"Report saved as {filename}")

if __name__ == "__main__":
    main()
