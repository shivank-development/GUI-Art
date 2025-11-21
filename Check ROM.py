import psutil

# Get disk usage info for the root directory (C:\ on Windows, / on Linux)
disk = psutil.disk_usage('/')

def convert_bytes(size):
    # Convert bytes to GB
    gb = size / (1024 ** 3)
    return gb

total_gb = convert_bytes(disk.total)
used_gb = convert_bytes(disk.used)
free_gb = convert_bytes(disk.free)

print(f"Total Storage (ROM): {total_gb:.2f} GB")
print(f"Used Storage: {used_gb:.2f} GB")
print(f"Free Storage: {free_gb:.2f} GB")
print(f"Storage Usage: {disk.percent}%")
