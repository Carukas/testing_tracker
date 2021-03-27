from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime
import re



from testing.models import Person, Tracking_entry, Orders

# Create your views here.


def start(request):

    orders_query_set=Orders.objects.all()

    persons_query_set=Person.objects.all()

    today=datetime.date.today()

    good_list=[]
    warning_list=[]
    danger_list=[]

    if len(persons_query_set)>0 and len(orders_query_set)>0:


        for person in persons_query_set:
            date=person.data
            person_type=person.tipas
            adjustment_value=int(Orders.objects.get(value=person_type).dienu_skaicius)
            adjusted_date=date + datetime.timedelta(days=adjustment_value)

            if (today - adjusted_date).days <0:
                good_list.append(person)
            if (today - adjusted_date).days >=0 and (today - adjusted_date).days <=3:
                warning_list.append(person)
            if(today - adjusted_date).days >3:
                danger_list.append(person)

        print(good_list)
        print(warning_list)
        print(danger_list)

    context={'warning_list':warning_list,
            'danger_list':danger_list,
            'orders':orders_query_set}

    return render(request, 'testing/index.html', context)

def valdzios_nurodymai(request):

    Nurodymai=Orders.objects.all()


    return render(request, 'testing/valdzios_nurodymai.html',{'Nurodymai':Nurodymai})

def valdzios_nurodymai_enter(request):

    Nurodymai=Orders.objects.all()

    if request.method=='POST':
        tipas=request.POST['tipas']
        skaicius=request.POST['skaicius']

        expression='[ąčęėįšųūžĄČĘĖĮŠŲŪŽ€]'
        value=re.sub(expression,'',tipas)
        value=value.replace(' ','_')
        value=value.replace('.','_')
        value=value.replace(',','_')

        Order_exist=Orders.objects.filter(tipas=tipas)
        Order_exist_number=len(Order_exist)

        if Order_exist_number>0:
            Order_update=Orders.objects.get(tipas=tipas)
            Order_update.dienu_skaicius=skaicius
            Order_update.save()

        else:

            Nurodymas=Orders(tipas=tipas, value=value, dienu_skaicius=skaicius)
            Nurodymas.save()




    return redirect("testing:valdzios_nurodymai")

def valdzios_nurodymai_update(request):

    Nurodymai=Orders.objects.all()

    if request.method=='POST':
        id_value=request.POST['id']
        skaicius=request.POST['skaicius']

        update_order=Orders.objects.get(id=id_value)
        update_order.dienu_skaicius=skaicius
        update_order.save()

    return redirect("testing:valdzios_nurodymai")


def enter_person(request):
    if request.method=='POST':

        name=request.POST['vardas']
        last_name=request.POST['pavarde']
        asmens_kodas=request.POST['asmens_kodas']
        person_type=request.POST['tipas']
        date=request.POST['data']

        Person_exist=Person.objects.filter(asmens_kodas=asmens_kodas)
        Person_exist_number=len(Person_exist)

        print(Person_exist)

        if Person_exist_number == 1:
            
            Person_exist=Person.objects.get(asmens_kodas=asmens_kodas)

            update_person_type=Person.objects.get(asmens_kodas=asmens_kodas)
            update_person_type.tipas=person_type
            update_person_type.save()

            update_person_date=Person.objects.get(asmens_kodas=asmens_kodas)
            update_person_date.data=date
            update_person_date.save()

            insert_track_record=Tracking_entry(vardas=Person_exist.vardas, pavarde=Person_exist.pavarde, asmens_kodas=asmens_kodas, veiksmas=person_type, data=date)
            insert_track_record.save()
        else:
            

            insert_person=Person(vardas=name, pavarde=last_name, asmens_kodas=asmens_kodas, tipas=person_type, data=date)
            insert_track_record=Tracking_entry(vardas=name, pavarde=last_name, asmens_kodas=asmens_kodas, veiksmas=person_type, data=date)

            insert_person.save()
            insert_track_record.save()


    return redirect("testing:start")


def update_person(request):
    if request.method=='POST':

        name=request.POST['vardas']
        last_name=request.POST['pavarde']
        asmens_kodas=request.POST['asmens_kodas']
        person_id=request.POST['id_number']
        person_type=request.POST['tipas']
        date=request.POST['data']

        update_person_type=Person.objects.get(id=person_id)
        update_person_type.tipas=person_type
        update_person_type.save()

        update_person_date=Person.objects.get(id=person_id)
        update_person_date.data=date
        update_person_date.save()


        insert_track_record=Tracking_entry(vardas=name, pavarde=last_name, asmens_kodas=asmens_kodas, veiksmas=person_type, data=date)
        insert_track_record.save()
        

    return redirect("testing:start")


def sarasas(request):

    Sarasu_variantai=Orders.objects.all()
    if request.method=='POST':
        tipas=request.POST['sarasas']
        tipas_exclude=request.POST['isskyrus']

        if tipas_exclude !="nieko_nepasirinkta":
            Sarasas_isskyrus=Tracking_entry.objects.filter(veiksmas=tipas_exclude).values('asmens_kodas')
            Sarasas_isskyrus=[d['asmens_kodas'] for d in Sarasas_isskyrus]
            print(Sarasas_isskyrus)

            Sarasas=Tracking_entry.objects.filter(veiksmas=tipas).exclude(asmens_kodas__in=Sarasas_isskyrus)
            return render(request, 'testing/sarasas.html',{'Sarasai':Sarasu_variantai,'Sarasas':Sarasas})

        else:
            Sarasas=Tracking_entry.objects.filter(veiksmas=tipas)
            return render(request, 'testing/sarasas.html',{'Sarasai':Sarasu_variantai,'Sarasas':Sarasas})
            

    return render(request, 'testing/sarasas.html',{'Sarasai':Sarasu_variantai})


