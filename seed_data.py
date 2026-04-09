import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  
django.setup()

from blog.models import Category, Post
import random

# Category lar yaratish
categories = [
    "Texnologiya",
    "Sport",
    "Ta'lim",
    "Yangiliklar"
]

category_objs = []

for name in categories:
    cat, created = Category.objects.get_or_create(name=name)
    category_objs.append(cat)

# Post uchun sample title va body
titles = [
    "Yangi texnologiyalar rivoji",
    "Futbol yangiliklari",
    "Django darslari",
    "Sun'iy intellekt kelajagi",
    "Python maslahatlari",
    "Ta'lim tizimidagi o'zgarishlar",
    "Sport musobaqalari",
    "Dasturlashni qanday o'rganish",
    "Startap g'oyalar",
    "IT yangiliklari"
]

bodies = [
    "Bu maqolada siz foydali ma'lumotlar olasiz.",
    "Bugungi kunda bu juda muhim mavzu hisoblanadi.",
    "Batafsil tushuntirish ushbu maqolada berilgan.",
    "Amaliy misollar bilan ko'rib chiqamiz.",
    "Yangi boshlovchilar uchun juda foydali."
]

# 20 ta post yaratish
for i in range(20):
    Post.objects.create(
        title=random.choice(titles) + f" #{i+1}",
        body=random.choice(bodies),
        category=random.choice(category_objs)
    )

print("✅ 4 ta kategoriya va 20 ta post yaratildi!")
