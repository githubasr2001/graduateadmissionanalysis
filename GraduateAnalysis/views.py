from django.shortcuts import render, redirect
import joblib
import numpy as np
from django.conf import settings
import os

# Assuming the model is correctly located and named
model_path = os.path.join(settings.BASE_DIR, 'randomforest.sav')
model = joblib.load(model_path)

def home(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        # Extracting each feature from the form
        serial_number = float(request.POST.get('serial_number', 0))
        gre_score = float(request.POST.get('gre_score', 0))
        toefl_score = float(request.POST.get('toefl_score', 0))
        university_rating = float(request.POST.get('university_rating', 0))
        sop = float(request.POST.get('sop', 0))
        lor = float(request.POST.get('lor', 0))
        cgpa = float(request.POST.get('cgpa', 0))
        research = float(request.POST.get('research', 0))

        # Make sure the feature array includes all 8 features
        features = np.array([[
            serial_number, gre_score, toefl_score, university_rating, sop, lor, cgpa, research
        ]])

        prediction = model.predict(features)
        prediction_percentage = round(prediction[0] * 100, 2)
        
        return render(request, 'result.html', {'prediction': prediction_percentage})
    else:
        return redirect('home')
