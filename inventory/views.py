from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages




def dashboard(request):
    return render(request, 'inventory/dashboard.html')



from django.template.loader import render_to_string
from django.http import JsonResponse


from django.template.loader import render_to_string
from django.http import JsonResponse


def new_stock(request):
    return render(request, 'inventory/new_stock.html')

import pandas as pd
from django.shortcuts import render

def new_stock(request):
    sheet_id = "1fDF6gQCLUr7k6V7d9QfBLwQdAVX_xpu_zip7XSUfFRI"
    sheet_name = "Sheet1"  # Eğer farklıysa değiştir
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        data = df.to_dict(orient="records")
    except Exception as e:
        data = []
        print("Google Sheet verisi okunamadı:", e)

    return render(request, 'inventory/new_stock.html', {'data': data})
