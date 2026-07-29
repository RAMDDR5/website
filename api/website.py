import urllib.request
with urllib.request.urlopen(RAW_URL) as response:
    code = response.read().decode("utf-8")
exec(code, {})
