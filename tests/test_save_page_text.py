# tests/test_save_page_text.py
# Test for saving page text using the WebAutomation agent
# Tests:
# - open browser
# - navigate to a page
# - save page text to a file
# - close browser

import sys
import os

# Add project root (browser-agent/) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_automation import WebAutomation

web = WebAutomation()

print(web.open_browser())
print(web.go_to("https://example.com"))
print(web.save_page_text("example.txt"))
print(web.close())

# End of file: tests/test_save_page_text.py
