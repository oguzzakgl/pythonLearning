# Konu: Platform Modülü
# Amaç: İşletim sistemi ve donanım hakkında bilgi alma.

import platform

print("Operating System:", platform.system())
print(dir(platform))
print("OS Version:", platform.version())
print("Machine Type:", platform.machine())
print("Processor Info:", platform.processor())
print("Python Version:", platform.python_version())

