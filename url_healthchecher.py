from urllib.parse import urlparse
import ipaddress

url = input("Enter URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "http://" + url

parsed = urlparse(url)
domain = parsed.netloc.lower()

print("\n===== URL Safety Report =====")

# HTTPS Check
if parsed.scheme == "https":
    print("[+] HTTPS: Yes")
else:
    print("[-] HTTPS: No")

# Domain
print("[+] Domain:", domain)

# IP Address Check
try:
    ipaddress.ip_address(domain.split(":")[0])
    print("[-] URL uses an IP address instead of a domain.")
except ValueError:
    print("[+] Domain name detected.")

# URL Shortener Check
shorteners = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "is.gd",
    "ow.ly"
]

if any(service in domain for service in shorteners):
    print("[-] URL Shortener Detected")
else:
    print("[+] No URL Shortener")

# Suspicious Keywords
keywords = [
    "login",
    "verify",
    "secure",
    "update",
    "bank",
    "paypal",
    "free",
    "gift"
]

found = [word for word in keywords if word in url.lower()]

if found:
    print("[-] Suspicious Keywords:", ", ".join(found))
else:
    print("[+] No Suspicious Keywords")

# URL Length
if len(url) > 75:
    print("[-] URL is unusually long.")
else:
    print("[+] URL length looks normal.")

print("\nBasic analysis complete.")