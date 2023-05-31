import pyshorteners

s = pyshorteners.Shortener()
long_url = input("Enter a long URL: ")
short_url = s.tinyurl.short(long_url)
print("Short URL: ", short_url)
