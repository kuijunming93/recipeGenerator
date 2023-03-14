from django.shortcuts import render
from . import services
from . import models
from django.views.generic import ListView
import json, random

# Create your views here.
def openai_api(context, cookie):
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
            imgURL = services.api_dalle(context.imgPrompt, " " + name)
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
        payload, imgURL, apiError = retrieve_repository()
    return payload, imgURL, apiError


def retrieve_repository():
    model = models.Recipe.objects.all()
    randInt = random.randrange(0, len(model))
    payload = model[randInt].content
    imgURL = model[randInt].imgPath
    return payload, imgURL, True

def recipe_view(request, pk):
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
        payload, imgURL, apiError = openai_api(context, request.session)
        # payload, imgURL, apiError = retrieve_repository()
        name = json.loads(payload)["name"]
    else:
        payload, imgURL, apiError = retrieve_repository()

    return render(request, './recipe.html', context={
        "generativeInfo":context,
        "payload": json.loads(payload),
        "imgLink": imgURL,
        "limitReached": limitReached,
        "apiError": apiError,
        "recentlyGenerated": request.session['generated'],
        "pageIndex": pk
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
    paginate_by = 3

    def get_queryset(self):
        return models.Recipe.objects.order_by('id')

def recipe_detail(request, pk):
    query = models.Recipe.objects.filter(id=pk).all()
    for item in query:
        context = item
        content = item.content
        print(content)
    return render(request, './recipe_detail.html', context={"context":context,"payload":json.loads(content)})

