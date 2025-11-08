import os
import django
from django.conf import settings
from django.urls import path
from django.shortcuts import render, redirect
from django.core.management import execute_from_command_line
from django.db import models
from django.contrib import admin

from django.urls import path, include

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY="abc123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],

    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "shop",
    ],

    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],

    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },

   
    CSRF_TRUSTED_ORIGINS=[
        "https://migold.onrender.com",
        "http://localhost:8000",
    ],

    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }],

    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
    STATIC_URL="/static/",

    # ✅ Add login redirects to fix login/logout
    LOGIN_URL="/accounts/login/",
    LOGIN_REDIRECT_URL="/",
    LOGOUT_REDIRECT_URL="/",
)


django.setup()

from shop.models import Product, Order
from django.contrib.auth.models import User  # <-- Add this

# --- CREATE SUPERUSER HERE ---
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin123"
    )
    print("Superuser created: username='admin', password='admin123'")

from shop.models import Product, Order


# --- Views ---
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def about(request):
    return render(request, "about.html")

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def buy(request, product_id):
    product = Product.objects.get(id=product_id)
    Order.objects.create(product=product)
    return redirect("/orders/")

def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

# --- URLs ---
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),  # include shop app URLs
    # Add this to enable login/logout pages
    
]




# --- Run Server ---
if __name__ == "__main__":
    from django.core.management import call_command

    call_command("makemigrations", "shop", interactive=False)
    call_command("migrate", interactive=False)




    # Seed products
   # Seed 20 products safely
products_to_add = [
    {"name": "Laptop", "price": 899.99, "description": "A powerful laptop", "image": "https://images.pexels.com/photos/18105/pexels-photo.jpg"},
    {"name": "Headphones", "price": 49.99, "description": "Noise-cancelling headphones", "image": "https://m.media-amazon.com/images/I/6151o2Kb8GL.jpg"},
    {"name": "Smartphone", "price": 499.99, "description": "Latest smartphone", "image": "https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg"},
    {"name": "Smartwatch", "price": 199.99, "description": "Fitness smartwatch", "image": "https://images.pexels.com/photos/267394/pexels-photo-267394.jpeg"},
    {"name": "Tablet", "price": 299.99, "description": "High-res tablet", "image": "https://images.pexels.com/photos/5077043/pexels-photo-5077043.jpeg"},
    {"name": "Camera", "price": 399.99, "description": "DSLR camera", "image": "https://in.canon/media/image/2024/07/17/3d47abeaf9574a9ba9401c6ff2ca7bb1_EOS+R5+Mark+II+%26+RF24-105mm+f4L+IS+USM+Front+Slant.png"},
    {"name": "Monitor", "price": 179.99, "description": "HD monitor", "image": "https://images.pexels.com/photos/572056/pexels-photo-572056.jpeg"},
    {"name": "Keyboard", "price": 49.99, "description": "Mechanical keyboard", "image": "https://images.pexels.com/photos/374074/pexels-photo-374074.jpeg"},
    {"name": "Mouse", "price": 29.99, "description": "Wireless mouse", "image": "https://images.pexels.com/photos/1334597/pexels-photo-1334597.jpeg"},
    {"name": "Printer", "price": 129.99, "description": "Laser printer", "image": "https://images.pexels.com/photos/3920125/pexels-photo-3920125.jpeg"},
    {"name": "Router", "price": 89.99, "description": "High-speed router", "image": "https://blog.teufelaudio.com/wp-content/uploads/2017/06/what-is-a-router.jpg.webp"},
    {"name": "Smart Speaker", "price": 99.99, "description": "Voice-controlled speaker", "image": "https://images.pexels.com/photos/374074/pexels-photo-374074.jpeg"},
    {"name": "External HDD", "price": 79.99, "description": "1TB external hard drive", "image": "https://www.securedatarecovery.com/Media/blog/2023/external-hard-drive.webp"},
    {"name": "USB Drive", "price": 19.99, "description": "64GB USB flash drive", "image": "https://images.pexels.com/photos/149070/pexels-photo-149070.jpeg"},
    {"name": "Smart Light", "price": 39.99, "description": "WiFi smart light", "image": "https://images.pexels.com/photos/374074/pexels-photo-374074.jpeg"},
    {"name": "Fitness Band", "price": 59.99, "description": "Track your activity", "image": "https://images.pexels.com/photos/277394/pexels-photo-277394.jpeg"},
    {"name": "Gaming Chair", "price": 199.99, "description": "Ergonomic chair", "image": "https://images.pexels.com/photos/696609/pexels-photo-696609.jpeg"},
    {"name": "Desk Lamp", "price": 29.99, "description": "LED desk lamp", "image": "https://images.pexels.com/photos/204611/pexels-photo-204611.jpeg"},
    {"name": "Projector", "price": 299.99, "description": "Mini home projector", "image": "https://images.pexels.com/photos/274973/pexels-photo-274973.jpeg"},
    {"name": "Webcam", "price": 69.99, "description": "HD webcam", "image": "https://images.pexels.com/photos/33923/pexels-photo.jpg"},
]

# --- Remove old products ---
# Product.objects.all().delete()



for p in products_to_add:
    Product.objects.get_or_create(name=p["name"], defaults=p)


execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])


