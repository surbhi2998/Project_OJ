import requests

def get_languages():
    url = "https://coderunner3.p.rapidapi.com/languages/"

    headers = {
        "X-RapidAPI-Host": "coderunner3.p.rapidapi.com",
        "X-RapidAPI-Key": "7664a0043cmshd67d5c3ab286110p140a9ajsn8c7708fbd3ce"
    }

    response = requests.request("GET", url, headers=headers)

    return (response.text)

languages={"Python":71,
            "Java":62,
            "C++":52,
            "Javascript":63}


def create_submissions(code,language,stdin=None):
    url = "https://coderunner3.p.rapidapi.com/submissions/"
    language_id= languages.get(language)

    querystring = {"base64_encoded":"false","wait":"true"}

    payload = {
        "language_id": language_id,
        "source_code": code,
        "stdin":stdin,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "coderunner3.p.rapidapi.com",
        "X-RapidAPI-Key": "7664a0043cmshd67d5c3ab286110p140a9ajsn8c7708fbd3ce"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return (response.json())
    # "stdout": "hi\n",
    # "time": "0.018",
    # "memory": 3340,
    # "stderr": null,
    # "token": "848b6e5a-d789-474d-9ca1-c9611398f960",
    # "compile_output": null,
    # "message": null,
    # "status": {
    #     "id": 3,
    #     "description": "Accepted"
    # }
