log_file = "access.log"

ip_count ={}
failed_login = {}

with open(log_file, "r") as file:
    for line in file:
        parts = line.split()


        ip = parts[0]

        ip_count[ip] = ip_count.get(ip, 0) + 1

        if "Failed" in line:
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

print("IP Activity count: ")
for ip, count in ip_count.items():
    print(ip, count)

print("\nFailed login Attempts: ")
for ip, count in failed_login.items():
    print(ip, count)

with open("suspicious_ips.txt", "w") as report:
    for ip, count in failed_login.items():
        if count >= 3:
            report.write(f"{ip} - {count} failed login attempts\n")

print("\nSuspicious IP report saved to suspicious_ips.txt")
