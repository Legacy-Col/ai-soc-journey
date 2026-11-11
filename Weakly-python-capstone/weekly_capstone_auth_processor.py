security_events = [
    {
        "username": "Collins",
        "status": "Failure",
        "ip_address": "192.168.1.25"
    },
    {
        "username": "John",
        "status": "Success",
        "ip_address": "10.0.0.15"
    },
    {
        "username": "Michael",
        "status": "Failure",
        "ip_address": "172.16.0.20"
    },
    {
        "username": "David",
        "status": "Failure",
        "ip_address": "192.168.1.25"
    },
    {
        "username": "Collins",
        "status": "Success",
        "ip_address": "192.168.1.25"
    },
    {
        "username": "John",
        "status": "Failure",
        "ip_address": "10.0.0.15"
    },
    {
        "username": "Peter",
        "status": "Success",
        "ip_address": "10.0.0.15"
    },

    {
        "username": "Collins", 
        "status": "Failure",
        "ip_address": "192.168.1.25"
    },

    {
        "username": "Collins", 
        "status": "Failure", 
        "ip_address": "192.168.1.25"
    },
    {
        "username": "Collins", 
        "status": "Failure", 
        "ip_address": "192.168.1.25"
    },
    {
        "username": "John", 
        "status": "Failure", 
        "ip_address": "10.0.0.15"
    },
    {
        "username": "Michael", 
        "status": "Failure", 
        "ip_address": "172.16.0.20"
    },
]

failed_attempts = 0
successful_attempts = 0
unknown_status_count = 0

unique_ips = set()

failed_counts = {}

overall_threshold = 5
ip_threshold = 3

suspicious_ip_found = False

for event in security_events:
    unique_ips.add(event["ip_address"])
    if event["status"] == "Failure":
        failed_attempts += 1
        failed_counts[event["ip_address"]] = failed_counts.get(event["ip_address"], 0) + 1
    elif event["status"] == "Success":
        successful_attempts += 1
    else:
        unknown_status_count += 1

if failed_attempts >= overall_threshold:
    classification = "Critical"
elif failed_attempts >= ip_threshold:
    classification = "Warning"
else:
    classification = "Normal"

print(f"Failed attempts: {failed_attempts}")
print(f"Successful attempts: {successful_attempts}")
print(f"Unique IP addresses: {len(unique_ips)}")
print("Unique IP addresses list:", unique_ips)
print("Failed attempts by IP address:")
for ip, count in failed_counts.items():
    print(f"  {ip}: {count}")
print(f"IP addresses with failed attempts above threshold ({ip_threshold}):")
for ip, count in failed_counts.items():
    if count >= ip_threshold:
        print(f"  {ip}: {count}")

print( "\n --- Security Events Summary --- " )
print("Total Events:", len(security_events))
print("Total Failed Attempts:", failed_attempts)
print("Total Successful Attempts:", successful_attempts)
print("Total Unique IP Addresses:", len(unique_ips))

print("\n--- Failed Attempts by IP Address ---")
for ip, count in failed_counts.items():
    print(f"IP Address: {ip}, Failed Attempts: {count}")

print(" \n Threat Analysis:", classification)

print(f"{classification}: An IP address has been detected with the threshold of more than {ip_threshold} failed attempts", end=" ")
for ip, count in failed_counts.items():
    if count >= ip_threshold:
        print(f"{ip}", end=". \n" )
   
    
print("\n --- individual IP Address Analysis --- ")
for ip, count in failed_counts.items():
    if count >= ip_threshold:
        suspicious_ip_found = True
        print(f"IP Address: {ip} has {count} failed attempts, which exceeds the threshold of {ip_threshold}.")

if suspicious_ip_found:
    print("Action Required: Immediate investigation needed for the above IP addresses.")
else:
    print("No IP addresses exceeded the threshold. No immediate action required.")