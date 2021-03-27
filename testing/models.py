from django.db import models

# Create your models here.

class Orders(models.Model):

    tipas=models.CharField(max_length=300) # Darbuotojo ivestas pavadinimas
    value=models.CharField(max_length=300) # Sugeneruotas pavadinimas
    dienu_skaicius=models.IntegerField() #Dienų skaičius iki kito įvedimo



    def __str__(self):
        return f'{self.tipas} {self.dienu_skaicius}'

class Person(models.Model):

    vardas=models.CharField(max_length=300) # Vardas
    pavarde=models.CharField(max_length=300) # Pavarde
    asmens_kodas=models.CharField(max_length=20) #Asmens kodas
    tipas=models.CharField(max_length=300, default='00000') # Tipas
    data=models.DateField() # Ivedimo data


    def __str__(self):
        return f'{self.pavarde} {self.vardas}'


class Tracking_entry(models.Model):

    vardas=models.CharField(max_length=300) # Vardas
    pavarde=models.CharField(max_length=300) # Pavarde
    asmens_kodas=models.CharField(max_length=20, default='00000') #Asmens kodas
    veiksmas=models.CharField(max_length=300) # Atliktas_veiksmas
    data=models.DateField() # Ivedimo data


    def __str__(self):
        return f'{self.pavarde} {self.vardas} {self.veiksmas}'

