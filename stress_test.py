import argparse
import psutil
import time


def get_cpu_usage():
    """Gets CPU usage percentage."""
    return psutil.cpu_percent()


def get_memory_usage():
    """Gets memory usage percentage."""
    return psutil.virtual_memory().percent


def get_io_wait():
    """Gets I/O wait percentage (corrected)."""
    return psutil.disk_io_counters().wait / 10  # Convert to milliseconds


def get_disk_usage():
    """Gets disk usage percentage for the root partition."""
    return psutil.disk_usage('/').percent


def run_stress_test(cpu_cores, mem_size, io_load, disk_load, duration):
    """Runs stress test based on user-provided options."""
    stress_cmd = []
    if cpu_cores:
        stress_cmd.append(f"--cpu {cpu_cores}")
    if mem_size:
        stress_cmd.append(f"--vm {mem_size}")
    if io_load:
        stress_cmd.append(f"--io {io_load}")
    if disk_load:
        stress_cmd.append(f"--hdd {disk_load}")

    if not stress_cmd:
        print("Error: No stress options provided. Please specify CPU, memory, I/O, or disk options.")
        return

    # Simulate stress test using psutil (not recommended for actual stress testing)
    # Replace with a real stress testing library if needed
    print(f"Running stress test for {duration} seconds...")
    start_time = time.time()
    while time.time() - start_time < duration:
        # Simulate some CPU and memory usage here
        time.sleep(0.1)

    print("Stress test completed.")


def main():
    parser = argparse.ArgumentParser(description="Kubernetes Stress Test Script")
    parser.add_argument("-c", "--cpu", type=int, help="Number of CPU cores to stress")
    parser.add_argument("-m", "--memory", type=str, help="Memory size (e.g., 1G) to stress")
    parser.add_argument("-i", "--io", type=int, help="I/O load for stress test")
    parser.add_argument("-d", "--disk", type=int, help="Disk load for stress test")
    parser.add_argument("-t", "--duration", type=int, required=True, help="Stress test duration in seconds")
    args = parser.parse_args()

    # Capture before test metrics
    print("** Before Stress Test **")
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage()}%")
    print(f"I/O Wait: {get_io_wait()} ms")
    print(f"Disk Usage: {get_disk_usage()}%")

    # Run stress test
    run_stress_test(args.cpu, args.memory, args.io, args.disk, args.duration)

    # Capture after test metrics (can be added within run_stress_test if needed)


if __name__ == "__main__":
    main()
