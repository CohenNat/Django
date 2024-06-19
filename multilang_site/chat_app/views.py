from django.shortcuts import render
from django.http import JsonResponse
import requests
import os

# Chargement des documents du corpus
corpus_dir = os.path.join(os.path.dirname(__file__), 'corpus')
documents = [open(os.path.join(corpus_dir, f), encoding='utf-8').read() for f in os.listdir(corpus_dir) if f.endswith('.txt')]

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = query_model(user_input)
        return render(request, 'chat_app/chatbot.html', {'response': response})
    return render(request, 'chat_app/chatbot.html')

def search_view(request):
    query = request.GET.get('query', '')
    search_results = []
    augmented_result = ""

    # Recherche dans le corpus local
    for doc in documents:
        if query.lower() in doc.lower():
            search_results.append(doc)

    # Utiliser le modèle de langage pour augmenter les résultats
    if query:
        augmented_result = query_model(query)

    context = {
        'query': query,
        'search_results': search_results,
        'augmented_result': augmented_result
    }

    return render(request, 'chat_app/search.html', context)

def query_model(query):
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    API_TOKEN = "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"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    response = requests.post(API_URL, headers=headers, json={"inputs": query})
    if response.status_code == 200:
        return response.json()
    else:
        return "Erreur lors de la génération de la réponse augmentée."
