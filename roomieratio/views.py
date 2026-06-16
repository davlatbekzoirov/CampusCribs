import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum 
from django.contrib.auth.models import User
from .models import Household, SharedExpense, ExpenseSplit, Chore
@login_required
def household_hub(request):
    household = request.user.households.first()
    
    if not household:
        if request.method == 'POST' and 'create_house' in request.POST:
            name = request.POST.get('name')
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            house = Household.objects.create(name=name, invite_code=code)
            house.members.add(request.user)
            return redirect('roomieratio:hub')
        return render(request, 'roomieratio/no_household.html')

    chores = household.chores.all()
    shared_expenses = household.shared_expenses.all()
    members = household.members.all()

    # Graph-Theory Simplification Backend Logic Simulation
    # For a deterministic calculation within standard views context:
    balances = []
    for member in members:
        paid = shared_expenses.filter(payer=member).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        owed = ExpenseSplit.objects.filter(expense__household=household, user=member).aggregate(Sum('amount_owed'))['amount_owed__sum'] or 0
        net = paid - owed
        balances.append({'user': member, 'net': net})

    if request.method == 'POST' and 'add_expense' in request.POST:
        title = request.POST.get('title')
        total = float(request.POST.get('total_amount'))
        split_type = request.POST.get('split_type') # EQUAL split scenario
        
        expense = SharedExpense.objects.create(household=household, payer=request.user, title=title, total_amount=total)
        share = total / members.count()
        for m in members:
            ExpenseSplit.objects.create(expense=expense, user=m, amount_owed=share)
        return redirect('roomieratio:hub')

    context = {
        'household': household,
        'chores': chores,
        'balances': balances,
        'members': members,
    }
    return render(request, 'roomieratio/hub.html', context)

@login_required
def complete_chore(request, chore_id):
    chore = get_object_or_404(Chore, id=chore_id, household__members=request.user)
    if request.method == 'POST':
        chore.is_completed = True
        if 'proof' in request.FILES:
            chore.proof_image = request.FILES['proof']
        chore.save()
    return redirect('roomieratio:hub')