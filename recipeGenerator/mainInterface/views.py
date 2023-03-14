from django.shortcuts import render
from . import services
from . import models
from django.views.generic import ListView
import json, random

# Create your views here.
def openai_api(context, cookie, preferredId, genMode):
    apiError = False
    try:
        prompt = context.textPrompt
        if len(cookie['generated']) > 0:
            prompt += " that is not "
            for i, el in enumerate(cookie['generated']):
                if i != len(cookie['generated']) - 1:
                    prompt += el + ", "
                else:
                    prompt += el

        print("prompt --> " + prompt)
        name, payload = services.api_chatgpt(prompt, 800, 0)
        if name is not None and name != "":
            imgPrompt = models.ImageType.objects.filter(id=genMode).all()[0].imgPrompt
            imgURL = services.api_dalle(imgPrompt, " " + name)
            models.Recipe.objects.create(
                name=name,
                imgPath=imgURL,
                content=payload
            )
            print(name)
            print(payload)
            print(imgURL)
            cookie['generated'].append(name)
    except:
        payload, imgURL, apiError = retrieve_repository(preferredId, genMode)
    return payload, imgURL, apiError


def retrieve_repository(preferredId = 1, genMode = 1):
    model = models.Recipe.objects.filter(recipeType=preferredId).filter(imgType=genMode).all()
    randObj = random.choice(model)
    payload = randObj.content
    imgURL = randObj.imgPath
    return payload, imgURL, True

def recipe_view(request, pk, genMode):
    limitReached = False
    context = models.GenerateType.objects.filter(id=pk).all()[0]
    if 'invokeCount' in request.session:
        if request.session['invokeCount'] < 10:
            request.session['invokeCount'] += 1
        else:
            limitReached = True
    else:
        request.session['invokeCount'] = 1
        request.session['generated'] = []

    if limitReached is not True:
        payload, imgURL, apiError = openai_api(context, request.session, pk, genMode)
        # payload, imgURL, apiError = retrieve_repository(pk, genMode)
        name = json.loads(payload)["name"]
    else:
        payload, imgURL, apiError = retrieve_repository(pk, genMode)

    return render(request, './recipe.html', context={
        "generativeInfo":context,
        "payload": json.loads(payload),
        "imgLink": imgURL,
        "limitReached": limitReached,
        "apiError": apiError,
        "recentlyGenerated": request.session['generated'],
        "pageIndex": pk,
        "genMode": genMode,
    })

class GenerateTypeListView(ListView):
    model = models.GenerateType
    fields = '__all__'
    context_object_name = 'generatetype_list'

    def get_queryset(self):
        return models.GenerateType.objects.order_by('id')

class RecipeListView(ListView):
    model = models.Recipe
    fields = '__all__'
    context_object_name = 'recipe_list'
    template_name = 'recipe_list.html'
    paginate_by = 2

    def get_queryset(self):
        return models.Recipe.objects.order_by('id')

def recipe_detail(request, pk):
    query = models.Recipe.objects.filter(id=pk).all()
    for item in query:
        context = item
        content = item.content
        print(content)
    return render(request, './recipe_detail.html', context={"context":context,"payload":json.loads(content)})

