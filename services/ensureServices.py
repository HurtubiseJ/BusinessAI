import os
import urllib.request
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def _check_url(url: str) -> bool:
    try:
        urllib.request.urlopen(url, timeout=2)
        return True
    except:
        return False

def ensureServices(services: list[str]):

    if "notionApi" in services:
        url = "http://localhost:8800/health"
        up = _check_url(url)

        if not up:
            print("Starting notionApi service...")
            subprocess.run(
                ["docker", "compose", "up", "-d", "notion-mcp"],
                cwd=os.path.join(BASE_DIR, 'services', "notion"), 
                check=True
            )

            print("Waiting for notion mcp health poll...")
            if not waitForService(url):
                print("Notion MCP service did not start in time.")

        else:
            print("notionApi service running...")

def waitForService(url: str, timeout: int = 10):
    start = time.time()
    while time.time() - start < timeout:
        try: 
            up = _check_url(url)
            if up:
                return True
        except: 
            pass
    return False