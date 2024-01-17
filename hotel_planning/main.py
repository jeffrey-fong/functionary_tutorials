import os

import requests


def call_hotels_com_provider_api(api_name: str, input_data: dict, rapidapi_key: str):
    urls = {
        "hotels_search": "https://hotels-com-provider.p.rapidapi.com/v2/hotels/search"
    }

    if urls.get(api_name):
        url = urls[api_name]
    else:
        print(f"Invalid API Name: `{api_name}`")
        return

    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=input_data)

    if response.status_code != 200:
        print(
            f"API call error: code-> {response.status_code} | message: {response.text}"
        )
        return

    results = response.json()

    if api_name == "hotels_search":
        results = results["properties"]
        final_res = []
        for result in results:
            final_res.append(
                {
                    "id": result["id"],
                    "name": result["name"],
                }
            )
        breakpoint()


if __name__ == "__main__":
    rapidapi_key = os.environ["RAPIDAPI_KEY"]
    input_data = {
        "region_id": "2872",
        "locale": "en_GB",
        "checkin_date": "2024-09-26",
        "sort_order": "REVIEW",
        "adults_number": "1",
        "domain": "AE",
        "checkout_date": "2024-09-27",
    }

    call_hotels_com_provider_api(
        api_name="hotels_search", input_data=input_data, rapidapi_key=rapidapi_key
    )