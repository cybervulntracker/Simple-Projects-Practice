import re
from collections import defaultdict

# Same idea as before—just recognizing a log pattern
LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} .*?) - (?P<level>\w+) - (?P<message>.*)'
)

def analyze_logs(log_text):
    """
    Instead of opening a file, we take logs as plain text.
    Useful when logs come from APIs, copy-paste, or live streams.
    """
    level_counts = defaultdict(int)
    error_messages = []
    total_lines = 0
    parsed_lines = 0

    # Split the text into lines (like reading a file, but in memory)
    lines = log_text.split("\n")

    for line in lines:
        total_lines += 1
        line = line.strip()

        if not line:
            continue  # skip empty lines

        match = LOG_PATTERN.match(line)

        if match:
            parsed_lines += 1
            data = match.groupdict()

            level = data["level"]
            message = data["message"]

            # Count log levels
            level_counts[level] += 1

            # Save errors for later
            if level.upper() == "ERROR":
                error_messages.append(message)

    return {
        "total_lines": total_lines,
        "parsed_lines": parsed_lines,
        "level_counts": dict(level_counts),
        "error_messages": error_messages
    }


def print_summary(summary):
    print("\n--- Log Summary ---")
    print(f"Total lines: {summary['total_lines']}")
    print(f"Parsed lines: {summary['parsed_lines']}")

    print("\nLevels:")
    for level, count in summary["level_counts"].items():
        print(f"  {level}: {count}")

    if summary["error_messages"]:
        print("\nErrors:")
        for err in summary["error_messages"][:5]:
            print(f"  - {err}")
    else:
        print("\nNo errors found 👍")


# Example usage (no file needed)
if __name__ == "__main__":
    logs = """
    2026-04-05 10:00:00,123 - INFO - Server started
    2026-04-05 10:01:00,456 - WARNING - High memory usage
    2026-04-05 10:02:00,789 - ERROR - Database connection failed
    2026-04-05 10:03:00,000 - INFO - Request processed
    """

    result = analyze_logs(logs)
    print_summary(result)