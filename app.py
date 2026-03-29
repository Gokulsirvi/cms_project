import os
from django.conf import settings

# ---------------- SETTINGS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY='secret',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
    ],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR],
        },
    ],
)

# ---------------- DJANGO SETUP ----------------
import django
django.setup()

# ---------------- VIEW ----------------
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("""
        <h1>Complaint Management System</h1>
        <p>This is a simple one-file Django app.</p>
        <form method="post" action="/submit/">
            <input type="text" name="title" placeholder="Complaint Title"><br><br>
            <textarea name="desc" placeholder="Description"></textarea><br><br>
            <button type="submit">Submit</button>
        </form>
    """)

def submit(request):
    if request.method == "POST":
        return HttpResponse("<h2>Complaint Submitted Successfully!</h2><a href='/'>Go Back</a>")
    return HttpResponse("Invalid Request")

# ---------------- URLS ----------------
urlpatterns = [
    path('', home),
    path('submit/', submit),
]

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "runserver"])
