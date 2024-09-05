
import requests


def request(api_url):
    resp = requests.get(api_url)
     # Raise an exception for any HTTP status code >= 400
    try:
        resp.raise_for_status()  # This will raise an HTTPError if the response status is not 200
        return resp.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle specific HTTP errors
        raise  # Re-raise the error to allow it to be handled upstream
    except Exception as err:
        print(f"Other error occurred: {err}")  # Handle other possible errors
        raise
