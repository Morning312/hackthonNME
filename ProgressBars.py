from tqdm import tqdm
import time

# Example: Tracking progress of multiple tasks
tasks = ["Task 1", "Task 2", "Task 3"]

for task in tasks:
    print(f"Starting {task}...")
    for i in tqdm(range(100), desc=task):
        time.sleep(0.05)  # Simulate work
    print(f"{task} completed!\n")