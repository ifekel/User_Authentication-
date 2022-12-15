from django.shortcuts import render, redirect
# Imported the redirect module 
from .models import Features

# Also imported the django.contrib.auth.models module
from django.contrib.auth.models import User, auth

# And lastly imported the messages module
from django.contrib import messages

# This is the home page at the start of the url
def index(request):
    # This gets the objects created in the Features models created in the admin page and shows in the htq
    feature = Features.objects.all()
    
    # {'feature': feature} enables us to access this variable in the our html file
    return render(request, 'index.html', {'feature': feature})



# This is a register function that works with the post method
def register(request):
    # If the request method is POST do the following
    if request.method == 'POST':    
        
        # gets the input value entered through the html form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cmdpwd']

        # Checks if the two passwords are the same
        if password == password2:
            # If they are the same run the following command
            # Filter through the db and check if the email entered already exists
            if User.objects.filter(email=email).exists():
                # If it does exist then flash the following message
                messages.info(request, 'Email address already exists')
                # Redirect the user back to the same page so as to show the messae
                return redirect('register')
            
            # Does the same thing as above
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username has already been used')
                return redirect('register')
            
            # If all passes as false then create a new account
            else:
                # Store the new account details in the db
                user = User.objects.create_user(username=username, email=email, password=password)
                # Save the new account
                user.save()
                # Redirect the user to the login page
                return redirect('login')
            
            # If the two passwords don't match,
        else:
            # Showo this messaae
            messages.info(request, 'passwords do not match')
            return redirect('register')
    else:
        # If the request method is not POST
        return render(request, 'register.html')
                
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Checing if the username and password exist in the database
        user = auth.authenticate(username=username, password=password)
        
        # If the user is found in the database redirect them to the home page
        if user is not None:
            auth.login(request, user)
            return redirect('/myapp/')
        else:
            # If the user is not found in the database redirect them back to the login page
            messages.info(request, 'Account not found!')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
    return render(request, 'login.html')
    


def logout(request):
    auth.logout(request)
    return redirect('/myapp/')


def counter(request):
    # Get the input entered in the form
    # text = request.POST['text']
    # Strp the input and count the number of it and add 1 to it
    # amount_of_words = len(text.split()) + 1
    # Return the amount variable to the html
    
    # Additional Featutres
    posts = [1, 2, 3, 4, 'Ifeanyi', 'Anthony', 'Mmeso', 'SoS']
    # {'amount': amount_of_words}, 
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
