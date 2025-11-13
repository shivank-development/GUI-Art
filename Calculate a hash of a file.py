import hashlib

def file_hash(file_path, algo="sha256"):
    h = hashlib.new(algo)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

file_path = "clcoding.txt"
print("SHA-256 Hash:", file_hash(file_path))
print("MD5 Hash:", file_hash(file_path, algo="md5"))



with open(file_path, "rb") as f:
    hash = hashlib.md5(f.read()).hexdigest()
print("MD5:", hash)