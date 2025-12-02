# test_simple_infinite_scroll.py
#
# Test for scrolling to the bottom of a page using the agent (simple version)
# Does not require credits & LLM
# Tests:
# - open broswer
# - navigate to a long page
# - scroll to bottom
# - close browser

import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_automation import WebAutomation

def main():
    print("\n=== Test: Scroll to Bottom ===")
          
    web = WebAutomation(use_chrome_profile=False)
    
    print("\n → Opening browser")
    print(web.open_browser())

    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    print(f"\n → Navigating to {url}")
    print(web.go_to(url))

    print("\n → Scrolling to bottom of page")
    result = web.simple_infinite_scroll()
    print(f"\n scroll_to_bottom result: {result}")

    print("\n → Closing browser")
    print(web.close())


if __name__ == "__main__":
    main()

# End of file: tests/test_simple_infinite_scroll.py