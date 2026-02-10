# 🔗 URL Shortener (CLI Version)
# ---------------------------------------------------
# Long URL → Tiny short URL
# TinyURL API use kar rahe hain
# ---------------------------------------------------

import requests   # API request bhejne ke liye


# 🔍 Shorten function
def shorten_url(long_url):

    # 🌍 TinyURL API endpoint
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"

    # 📡 GET request bhejo
    response = requests.get(api_url)

    # ✅ Agar success
    if response.status_code == 200:
        return response.text
    else:
        return "❌ Error shortening URL"


# 🚀 Start program
url = input("Enter long URL: ")

short = shorten_url(url)

print("\n🔗 Short URL:", short)