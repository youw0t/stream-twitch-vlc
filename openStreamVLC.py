import subprocess
import json
import sys

channel_url = 'twitch.tv/' + input("Enter streamer name (for example: summit1g): \n")
vlcloc = ''
with open('settings.txt', 'r') as settings:
    for line in settings:
        li = line.strip()
        if not li.startswith("#"):
            if '\\' in li:
                print("Replace all '\' with '/'")
                sys.exit(1)
            else:
                vlcloc = li

def getURL():
    try:
        output = subprocess.Popen(["livestreamer", "--http-header", "Client-ID=xn6bnxnzg4k4aircca8km0w2u7gdk1", channel_url, "-j"], stdout=subprocess.PIPE).communicate()[0]
    except subprocess.CalledProcessError:
        print("Error occured getting stream data, make sure stream is online and channel name is spelled correctly")
        sys.exit(1)
    except OSError:
        print("Error with livestreamer package, make sure it is installed correctly and Python is added to PATH")


    try:
        url = json.loads(output)['streams']['720p60']['url']
    except (ValueError, KeyError):
        print("Error occured getting stream data, make sure stream is online and channel name is spelled correctly")
        sys.exit(1)

    return url

def loadVLC(url):
    try:
        start = subprocess.Popen([vlcloc, url], stdout=subprocess.PIPE).communicate()[0]
    except Exception as e:
        print("Error loading stream into VLC: ", e)
        sys.exit(1)
        

if __name__ == '__main__':
    url = getURL()
    loadVLC(url)
    
    



    


