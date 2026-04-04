import re

def validate_ip(ip):
    # Pattern for IPv4
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    
    if not re.match(pattern, ip):
        return f"❌ '{ip}' doesn’t even look like a valid IPv4 format. Did you mistype it?"

    parts = ip.split(".")

    for i, part in enumerate(parts):
        num = int(part)

        if num < 0 or num > 255:
            return f"❌ Hmm... the {i+1}th segment '{part}' is out of range (0–255). That’s not allowed in IPv4."

        if part.startswith("0") and len(part) > 1:
            return f"⚠️ Segment '{part}' has a leading zero. Technically suspicious — better avoid that."

    # Extra human-style observations
    if ip == "127.0.0.1":
        return f"✅ '{ip}' is valid! That’s your localhost — your computer talking to itself 😄"

    if ip.startswith("192.168"):
        return f"✅ '{ip}' is valid! Looks like a private network IP (probably your WiFi router setup)."

    if ip.startswith("8.8.8.8"):
        return f"✅ '{ip}' is valid! That’s Google DNS — a popular and reliable one."

    return f"✅ '{ip}' is a perfectly valid IPv4 address. Nothing suspicious here 👍"


# Example usage
ips = [
    "192.168.1.1",
    "256.100.50.0",
    "123.045.067.089",
    "127.0.0.1",
    "8.8.8.8",
    "abc.def.ghi.jkl"
]

for ip in ips:
    print(validate_ip(ip))