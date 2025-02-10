import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    data = {}

    if mock:
        # linkedin_profile_url = ""
        # response = requests.get(
        #     linkedin_profile_url,
        #     timeout=10,
        # )

        try:
            with open("packages/data.json", "r", encoding="utf-8") as file:
                d = json.load(file)
                data = d.get("person")
            # print("JSON loaded successfully:", data)
        except FileNotFoundError:
            print("Error: File not found!")
        except json.JSONDecodeError:
            print("Error: Invalid JSON!")

    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

        data = response.json().get("person")

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    # print(data)

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile_url="", mock=True),
    )
