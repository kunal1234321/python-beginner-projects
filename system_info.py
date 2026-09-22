import platform
import os

print("SYSTEM INFORMATION")
print("-" * 30)

print("Operating system:", platform.system())
print("OS version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Python version:", platform.python_version())
print("CPU cores:", os.cpu_count())