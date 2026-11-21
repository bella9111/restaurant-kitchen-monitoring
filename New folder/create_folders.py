import os

folders = [
    "producer",
    "nifi-flow",
    "spark-job",
    "database",
    "dashboard"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep = os.path.join(folder, ".gitkeep")
    with open(gitkeep, "w") as f:
        f.write("")

print("Folders created successfully.")