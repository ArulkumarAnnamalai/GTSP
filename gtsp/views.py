from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Standard, Protocol, RegulatoryRequirement

def base(request):
    return render(request,"base.html")        

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


@login_required
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_page')

    return redirect('dashboard')

@login_required
def dashboard(request):
    context = {
        'standards_count': Standard.objects.count(),
        'protocols_count': Protocol.objects.count(),
        'regulations_count': RegulatoryRequirement.objects.count(),
    }

    return render(request, 'dashboard.html', context)

@login_required
def protocols(request):
    protocols = Protocol.objects.all().order_by('-created_at')
    return render(request, 'protocols.html', {'protocols': protocols})


@login_required
def add_protocol(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if name and description:
            Protocol.objects.create(
                name=name,
                description=description
            )
            messages.success(request, 'Protocol added successfully.')
            return redirect('protocols_page')

        messages.error(request, 'Please fill in all fields.')

    return render(request, 'protocol_form.html')


@login_required
def edit_protocol(request, id):
    protocol = get_object_or_404(Protocol, id=id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if name and description:
            protocol.name = name
            protocol.description = description
            protocol.save()
            messages.success(request, 'Protocol updated successfully.')
            return redirect('protocols_page')

        messages.error(request, 'Please fill in all fields.')

    return render(
        request, 'protocol_form.html', {'protocol': protocol}
    )


@login_required
def delete_protocol(request, id):
    if request.method == 'POST':
        protocol = get_object_or_404(Protocol, id=id)
        protocol.delete()
        messages.success(request, 'Protocol deleted successfully.')

    return redirect('protocols_page')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not email or not password:
            messages.error(request, 'All fields are required.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')

        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'Registration successful.')
            return redirect('login_page')

    return render(request, 'register.html')

@login_required
def regulations(request):
    regulations = RegulatoryRequirement.objects.all().order_by('-created_at')
    return render(
        request, 'regulations.html', {'regulations': regulations}
    )


@login_required
def add_regulation(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title and description:
            RegulatoryRequirement.objects.create(
                title=title,
                description=description
            )
            messages.success(request, 'Regulation added successfully.')
            return redirect('regulations_page')

        messages.error(request, 'Please fill in all fields.')

    return render(request, 'regulation_form.html')


@login_required
def edit_regulation(request, id):
    regulation = get_object_or_404(RegulatoryRequirement, id=id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title and description:
            regulation.title = title
            regulation.description = description
            regulation.save()
            messages.success(request, 'Regulation updated successfully.')
            return redirect('regulations_page')

        messages.error(request, 'Please fill in all fields.')

    return render(
        request, 'regulation_form.html', {'regulation': regulation}
    )


@login_required
def delete_regulation(request, id):
    if request.method == 'POST':
        regulation = get_object_or_404(RegulatoryRequirement, id=id)
        regulation.delete()
        messages.success(request, 'Regulation deleted successfully.')

    return redirect('regulations_page')

@login_required
def standards(request):
    standards = Standard.objects.all().order_by('-created_at')

    return render(
        request,
        'standards.html',
        {'standards': standards}
    )  

@login_required
def add_standard(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if name and description:
            Standard.objects.create(
                name=name,
                description=description
            )
            messages.success(request, 'Standard added successfully.')
            return redirect('standards_page')

        messages.error(request, 'Please fill in all fields.')

    return render(request, 'standard_form.html')

@login_required
def edit_standard(request, id):
    standard = get_object_or_404(Standard, id=id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if name and description:
            standard.name = name
            standard.description = description
            standard.save()

            messages.success(request, 'Standard updated successfully.')
            return redirect('standards_page')

        messages.error(request, 'Please fill in all fields.')

    return render(
        request,
        'standard_form.html',
        {'standard': standard}
    )

@login_required
def delete_standard(request, id):
    if request.method == 'POST':
        standard = get_object_or_404(Standard, id=id)
        standard.delete()
        messages.success(request, 'Standard deleted successfully.')

    return redirect('standards_page')

