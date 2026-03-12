ip_count = {}

with open ("access.log") as file:
    for line in file:
        ip = line.split()[0]

        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

print("IP Activity Summary:\n")

for ip, count in ip_count.items():
    print(ip, "->", count, "attempts")

    if count >= 3:
        print("Suspicious activity detected from:", ip)
