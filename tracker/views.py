from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from .forms import MealForm

def meal_list(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm()

    meals = Meal.objects.all()
    return render(request, 'tracker/meal_list.html', {'meals': meals, 'form': form})

def update_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm(instance=meal)
    return render(request, 'tracker/update_meal.html', {'form': form, 'meal': meal})

def delete_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('meal_list')
    return render(request, 'tracker/delete_meal.html', {'meal': meal})