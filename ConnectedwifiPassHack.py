import subprocess
import re

def get_wifi_profiles():
    output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
    return profiles

def get_wifi_password(profile):
    output = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True).stdout
    password = re.search(r"Key Content\s*:\s*(.*)", output)
    if password:
        return password.group(1)
    else:
        return None

def main():
    profiles = get_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    print("{:<30} | {}".format("Wi-Fi Name", "Password"))
    print("-" * 50)
    for profile in profiles:
        password = get_wifi_password(profile)
        print("{:<30} | {}".format(profile, password if password else "N/A"))

if __name__ == "__main__":
    main()
