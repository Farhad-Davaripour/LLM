import os
import requests
from configparser import ConfigParser

parser = ConfigParser()
_ = parser.read("C:\\Users\\Farhad.Davaripour\\LLM\\.cfg.ini")

# gpt3 api key
proxy_curl_api_key = parser.get("proxy_curl_api_key", "api_key")

os.environ["proxy_curl_api_key"] = parser.get("proxy_curl_api_key", "api_key")


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape the information from the linkedin profile.
    Manually scrape the information from linkedin
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ["proxy_curl_api_key"]}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", 
                      "certifications", 
                      "profile_pic_url", 
                      "recommendations", 
                      "volunteer_work", 
                      "description", 
                      "url",
                      "background_cover_image_url",
                      "occupation",
                      "skill_ratings",
                      "projects",
                      "endorsements",
                      "publications",
                      "additional_info",
                      "interests",
                      "honors_awards",
                      "test_scores",
                      "languages",
                      "extracurricular_activities",
                      "patents"
                      ]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
