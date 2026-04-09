import time

# Fake cloud resources
resources = [
    {"id": "bucket1", "type": "S3", "public": True},
    {"id": "sg1", "type": "SecurityGroup", "open": True}
]

# Logger
def log(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

# Fix functions
def fix_s3(r):
    r["public"] = False
    msg = f"Fixed: {r['id']} public access removed"
    print(msg)
    log(msg)

def fix_sg(r):
    r["open"] = False
    msg = f"Fixed: {r['id']} port closed"
    print(msg)
    log(msg)

# Scanner
def scan():
    print("\nScanning cloud...\n")
    log("Scan started")

    for r in resources:
        if r["type"] == "S3" and r["public"]:
            msg = f"Violation: {r['id']} is public"
            print(msg)
            log(msg)
            fix_s3(r)

        if r["type"] == "SecurityGroup" and r["open"]:
            msg = f"Violation: {r['id']} is open"
            print(msg)
            log(msg)
            fix_sg(r)

    log("Scan completed")

# Continuous monitoring
while True:
    scan()
    time.sleep(10)