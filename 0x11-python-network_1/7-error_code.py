import requests
import sys
"""
error code
"""

if __name__ == "__main__":
    
    try:
        response = requests.get(sys.argv[1])

        
        print(response.text)
    
    except Exception as err:
        print("Error code: {}".format(response.status_code))