import re

print("Suspicious URL Detector")

# Main program loop
while True:
    url = input("\nEnter a URL: ").strip()

    if url.lower() == "exit":
        print("Goodbye!")
        break

    reasons = []

    # Check if URL starts correctly
    if not url.startswith("http://") and not url.startswith("https://"):
        reasons.append("URL does not start with http:// or https://")

    # Check for IP address
    if re.search(r'https?://\d+\.\d+\.\d+\.\d+', url):
        reasons.append("Uses an IP address instead of a domain")

    # Check for @ symbol
    if "@" in url:
        reasons.append("Contains '@' symbol — may be hiding real address")

    # Check if URL is too long
    if len(url) > 75:
        reasons.append("URL is very long")

    # Look for suspicious words
    suspicious_words = ["login", "update", "verify", "bank", "secure"]
    for word in suspicious_words:
        if word in url.lower():
            reasons.append(f"Contains suspicious word: '{word}'")

    # Show results
    print("\n--- Result ---")
    if len(reasons) == 0:
        print("This URL looks OK (no red flags found).")
    else:
        print("WARNING: Suspicious URL detected!")
        for r in reasons:
            print("-", r)






