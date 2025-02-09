import hashlib
import os
import time

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """Calculate the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    return hash_func.hexdigest()

def monitor_file(file_path, interval=10):
    """Monitor a file for changes by comparing its hash periodically."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    initial_hash = calculate_file_hash(file_path)
    if initial_hash is None:
        return

    print(f"Monitoring file: {file_path}")
    print(f"Initial hash: {initial_hash}")

    try:
        while True:
            time.sleep(interval)
            current_hash = calculate_file_hash(file_path)
            if current_hash is None:
                continue

            if current_hash != initial_hash:
                print(f"File {file_path} has changed!")
                print(f"New hash: {current_hash}")
                initial_hash = current_hash
            else:
                print(f"No changes detected in {file_path}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    # Take file path input from the user
    file_to_monitor = input("Enter the full path to the file you want to monitor: ")
    monitor_file(file_to_monitor, interval=5)  # Check every 5 seconds