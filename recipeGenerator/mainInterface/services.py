secret_key = "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"
imgbb_secret = "NDFkM2FjMWMwMjIyZTU4NTRjMDhmZDZiNDZlNjRiOTcK"
#41d3ac1c0222e5854c08fd6b46e64b97

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
    output = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        response_format="b64_json"
    )

    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": base64.b64decode(imgbb_secret),
        "image": output["data"][0]["b64_json"]
    }
    res = requests.post(url, payload)
    return json.loads(res.text)["data"]["image"]["url"]

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


