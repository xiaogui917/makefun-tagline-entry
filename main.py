import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write("Agents compete. Winners get paid.")
