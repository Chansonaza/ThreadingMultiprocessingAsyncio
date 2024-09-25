import threading
import time

def simulate_io_task(file_name, duration):
  print(f"Processing {file_name} for {duration} seconds.....")
  time.sleep(duration)
  print(f"Completed {file_name} processing")

def run_io_tasks():
  threads = []
  for i in range(6):
    thread = threading.Thread(target=simulate_io_task, args=(f"file_{i}.txt", 3))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()