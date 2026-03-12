failed_attempts = {}

with open ("access.log") as file:
    for line in file:
        parts = line.split()

        ip = parts[0]
        status = parts[1]

        if status == "login_failed":

            if ip in failed_attempts: failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("\nFailed Login Summary:\n")

for ip, count in failed_attempts.items():

    print(ip, "->", count, "failed attempts")

    if count >= 3:
        print("Possible brute force attack from:", ip)
