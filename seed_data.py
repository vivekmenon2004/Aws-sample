"""Seed sample brands and phones into the database."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phonestore.settings')
django.setup()

from phones.models import Brand, MobilePhone

# Clear existing data
MobilePhone.objects.all().delete()
Brand.objects.all().delete()

# Brands
samsung = Brand.objects.create(name='Samsung')
apple   = Brand.objects.create(name='Apple')
oneplus = Brand.objects.create(name='OnePlus')

# Phones
MobilePhone.objects.create(brand=samsung, model_name='Galaxy S24 Ultra', price=1199.99,
    storage='256GB', ram='12GB', battery='5000mAh', condition='new', in_stock=True)
MobilePhone.objects.create(brand=samsung, model_name='Galaxy A55', price=449.99,
    storage='128GB', ram='8GB', battery='5000mAh', condition='new', in_stock=True)
MobilePhone.objects.create(brand=apple, model_name='iPhone 15 Pro', price=999.99,
    storage='256GB', ram='8GB', battery='3274mAh', condition='new', in_stock=True)
MobilePhone.objects.create(brand=apple, model_name='iPhone 14', price=749.99,
    storage='128GB', ram='6GB', battery='3279mAh', condition='used', in_stock=True)
MobilePhone.objects.create(brand=oneplus, model_name='OnePlus 12', price=799.99,
    storage='256GB', ram='12GB', battery='5400mAh', condition='new', in_stock=False)

print("✅ Sample data seeded successfully!")
print(f"   Brands: {Brand.objects.count()}")
print(f"   Phones: {MobilePhone.objects.count()}")
