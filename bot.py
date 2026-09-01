import os
import random
import subprocess
from datetime import datetime

# Configurations
SKIP_CHANCE = 0.01  # 1% chance to skip the day entirely
MIN_COMMITS = 10
MAX_COMMITS = 70
LOG_FILE = "activity_log.txt"
GIT_AUTHOR_NAME = os.environ.get("GIT_AUTHOR_NAME", "1tobiasmm")
GIT_AUTHOR_EMAIL = os.environ.get(
    "GIT_AUTHOR_EMAIL", "178795395+1tobiasmm@users.noreply.github.com"
)


def run_command(command):
    """Helper to execute shell commands securely."""
    subprocess.run(command, shell=True, check=True)


def main():
    # 1. Roll the dice for the 1% skip chance
    if random.random() < SKIP_CHANCE:
        print("Skipping today's commits based on the 1% random chance.")
        return

    # 2. Determine how many commits to make today
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    print(f"Preparing to make {num_commits} commits today...")

    # Configure this repository's identity to an email verified by the owner.
    subprocess.run(
        ["git", "config", "--local", "user.name", GIT_AUTHOR_NAME], check=True
    )
    subprocess.run(
        ["git", "config", "--local", "user.email", GIT_AUTHOR_EMAIL], check=True
    )

    # 3. Loop and create individual commits
    for i in range(1, num_commits + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append a unique line to the file to create a change
        with open(LOG_FILE, "a") as f:
            f.write(f"Record update {i}/{num_commits} at {timestamp}\n")

        # Stage and commit the change
        run_command(f"git add {LOG_FILE}")
        run_command(
            f'git commit -m "update: sync activity log [{i}/{num_commits}]"'
        )

    print("All local commits completed successfully.")


if __name__ == "__main__":
    main()
