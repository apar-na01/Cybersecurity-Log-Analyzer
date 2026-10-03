with open("sample.log", "r") as file:
    logs = file.readlines()

print("=== Cybersecurity Log Analyzer ===")

# Total log entries
total_logs = len(logs)
print("Total log entries:", total_logs)

# Count failed login attempts
failed_logins = 0

for log in logs:
    if "LOGIN FAILED" in log:
        failed_logins += 1

print("Failed login attempts:", failed_logins)

# Count successful login attempts
successful_logins = 0

for log in logs:
    if "LOGIN SUCCESS" in log:
        successful_logins += 1

print("Successful login attempts:", successful_logins)

# Count failed logins by user
failed_users = {}

for log in logs:
    if "LOGIN FAILED" in log:
        parts = log.strip().split("user=")
        username = parts[1]

        if username in failed_users:
            failed_users[username] += 1
        else:
            failed_users[username] = 1

print("\n=== Failed Login Attempts by User ===")

for user, count in failed_users.items():
    print(user, ":", count)

# Security analysis
print("\n=== Security Analysis ===")

suspicious_users = 0

for user, count in failed_users.items():
    if count >= 3:
        print("WARNING:", user, "has", count, "failed login attempts.")
        suspicious_users += 1

if suspicious_users == 0:
    print("No suspicious login pattern detected.")
else:
    print("\nSuspicious users detected:", suspicious_users)

print("\n=== Analysis Complete ===")
