import os
secret_key = os.getenv("OPENAI_API_KEY")
imgUpload_secret = os.getenv("GH_API_KEY")

import openai
import requests
import json
import re, base64, uuid, pathlib

openai.api_key = secret_key

def extractJson(content):
    regex = r"({.*})"
    matched = re.search(regex, content.replace('\n', ''))
    return matched.group(1)

def api_chatgpt(prompt, token, temp):
    output = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=token,
        temperature=temp
    )
    name = json.loads(extractJson(output["choices"][0]["text"]))["name"]
    print(json.loads(extractJson(output["choices"][0]["text"])))
    return name, extractJson(output["choices"][0]["text"])

def api_dalle(initPrompt, promptName):
    prompt = initPrompt + promptName
    print("dall-e prompt --> " + prompt)
    output = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
        response_format="b64_json"
    )

    print("dall-e success")
    UUID = str(uuid.uuid4().hex)
    url = "https://api.github.com/repos/kuijunming93/imgUpload/contents/img-" + UUID +".jpg"
    headers = {
        "Authorization": f'''Bearer {imgUpload_secret}''',
        "Content-type": "application/vnd.github+json"
    }
    data = {
        "message": "Upload " + UUID,
        "content": output["data"][0]["b64_json"]
    }
    res = requests.put(url, headers=headers, json=data)

    print("gh res -> " + res.text)
    imgURL = json.loads(res.text)['content']['download_url']
    print(imgURL)

    return imgURL

def save_as_img(api_response):
    DATA_DIR = pathlib.Path.cwd() / "temp" / "json"
    IMAGE_DIR = pathlib.Path.cwd() / "temp" / "images"
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    fileName = uuid.uuid4().hex
    fileName_json = DATA_DIR / f"{fileName}.json"

    with open(fileName_json, mode="w", encoding="utf-8") as file:
        json.dump(api_response, file)

    with open(fileName_json, mode="r", encoding="utf-8") as file:
        processed = json.load(file)

    for index, image_dict in enumerate(processed["data"]):
        image_data = base64.b64decode(image_dict["b64_json"])
        image_file = IMAGE_DIR / f"{fileName}.jpg"
        with open(image_file, mode="wb") as jpg:
            jpg.write(image_data)


