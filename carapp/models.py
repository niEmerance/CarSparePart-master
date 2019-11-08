from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CarCategory(models.Model):
    categoryName=(
        ('Toyota','Toyota'),
        ('Cross country','Cross country'),
        ('Vox wagen','Vox wagen'),
        ('Suzuki','Suzuki'),
        ('Mahindra','Mahindra'),
        ('Honda','Honda'),
        ('Hyunda','Hyunda'),
        ('Volvo','Volvo'),
        ('Daihatsu','Daihatsu'),
        
    )
    categoryPart=models.CharField(max_length=40,choices=categoryName)
    categoryImage=models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryPart




class SpareParts(models.Model):
    nameChoose=(('Head lights','Head lights'),
        ('Brake lights','Brake lights'),
        ('Tail lights','Tail lights'),
        ('Tail gate','Tail gate'),
        ('Mirrors','Mirrors'),
        ('Hoods','Hoods'),
        ('Window','Window'),
        ('Door','Door'),
        ('Tire','Tire'),
        ('Petrol tank','Petrol tank'),
        ('Roof','Roof'),
        ('Steering wheel','Steering wheel'),
        ('Engine','Engine'),
        
    )
    namePart=models.CharField(max_length=40,choices=nameChoose)
    price=models.IntegerField()
    locationChoose=(
        ('Gatsata','Gatsata'),
        ('Nyamirambo','Nyamirambo'),
        ('Remera','Remera'),
        ('Nyabugogo','Nyabugogo'),
        )
    locationPart=models.CharField(max_length=40,choices=locationChoose)
    ImagePart=models.ImageField(upload_to='spareparts/')
    Phone=models.IntegerField()
    carCat = models.ManyToManyField(CarCategory)
    

    def __str__(self):
        return self.namePart


class Cart(models.Model):
    sparePart=models.ManyToManyField(SpareParts,null=True,blank=True)
    total=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    
    # def __str__(self):
    #     return self.id

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profiles/')
    country= models.TextField(max_length =100)
    contact=models.IntegerField(default=None, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.country

    def save_profile(self):
        self.save()