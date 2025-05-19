from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import joblib
import numpy as np
from .serializers import PredictionRequestSerializer

model_rec = joblib.load('C:\\Users\\HP\\Downloads\\integration ml\\django api\\api\\models\\trained_models\\model_recettes.pkl')
model_dep = joblib.load('C:\\Users\\HP\\Downloads\\integration ml\\django api\\api\\models\\trained_models\\model_depenses.pkl')
le = joblib.load('C:\\Users\\HP\\Downloads\\integration ml\\django api\\api\\models\\trained_models\\label_encoder.pkl')

def home(request):
    return render(request, 'index.html')

@csrf_exempt
@api_view(['POST'])
def predict_budget(request):
    print("✅ Données reçues :", request.data)
    serializer = PredictionRequestSerializer(data=request.data)
    if serializer.is_valid():
        commune = serializer.validated_data['commune']
        annee = serializer.validated_data['annee']

        try:
            commune_encoded = le.transform([commune])[0]
        except ValueError:
            return Response({"error": "Commune inconnue."}, status=status.HTTP_400_BAD_REQUEST)

        X = np.array([[annee, commune_encoded]])
        recettes = model_rec.predict(X)[0]
        depenses = model_dep.predict(X)[0]

        return Response({
            "commune": commune,
            "annee": annee,
            "recettes": round(recettes, 2),
            "depenses": round(depenses, 2)
        })

    print("❌ Erreurs serializer :", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
