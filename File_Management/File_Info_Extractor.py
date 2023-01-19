import os
import hashlib
import datetime
import pytz

# File path
file_path = "C:\Code\Python\File_Management\Thisisasamplefile.txt"

# File size
file_size = os.path.getsize(file_path)

# File modification time
mod_time = os.path.getmtime(file_path)

# File creation time
creation_time = os.path.getctime(file_path)

# Hash file value
hasher = hashlib.sha256()
with open(file_path, 'rb') as f:
    buf = f.read()
    hasher.update(buf)
hash_value = hasher.hexdigest()

# Convert to New Zealand time
nz_timezone = pytz.timezone("Pacific/Auckland")
mod_time_nz = datetime.datetime.fromtimestamp(mod_time, nz_timezone)
creation_time_nz = datetime.datetime.fromtimestamp(creation_time, nz_timezone)

print("File path:", file_path)
print("File size:", file_size)
print("Modified date:", mod_time_nz)
print("Creation date:", creation_time_nz)
print("Hash value:", hash_value)
