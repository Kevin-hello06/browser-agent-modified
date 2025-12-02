# tests/test_auto_accept_cookies.py
# Test for auto accepting cookies using the WebAutomation agent
# Tests:
# - open browser
# - navigate to a page
# - auto accept cookies
# - close browser

import sys
import os

# Add project root (browser-agent/) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_automation import WebAutomation

web = WebAutomation()

print(web.open_browser())
print(web.go_to("https://www.theguardian.com"))
print(web.auto_accept_cookies())
print(web.close())

# End of file: tests/test_auto_accept_cookies.py
