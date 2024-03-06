from django.db import IntegrityError, connection
from django.shortcuts import render

from .models import Func

#Assuming id's will be available through request.Here we are using dummy variables for id's.

def check(request):
    raw_query = 'SELECT * FROM assignment_func'
    lst = Func.objects.raw(raw_query)
    return render(request,'index.html',{'lst':lst})

def see(request): #for viewing the current details of all devices belong to this company
    company_id = 2
    raw_query = 'SELECT * FROM assignment_device WHERE company_id_id=%s'

    try:
        with connection.cursor() as cursor:
            cursor.execute(raw_query, [company_id])
            lst = cursor.fetchall()
            print(lst[0])
    except Exception as e:
        print(f"Error during query execution: {e}")
        lst = []  # Handle the case where an error occurred
    
    return render(request,'index.html',{'lst':lst})

def InsertLog(request): #this funtion will be executed when an employee checks out any asset.
    company_id = 1
    device_id = 1
    employee_id = 1

    raw_query = """
        INSERT INTO assignment_devicelog (employee_id_id, company_id_id, device_id_id, check_out_condition, check_out_date)
        VALUES (%s, %s, %s, (SELECT device_condition FROM assignment_device WHERE id = %s AND company_id_id = %s), NOW())
    """
    raw_query2 = """
        update assignment_device set check_out_date=NOW(),occupied=%s where company_id_id=%s and 
        id=%s
    """

    try:
        # Execute the raw query
        print('ya')
        with connection.cursor() as cursor:
            cursor.execute(raw_query, [employee_id, company_id, device_id, device_id, company_id])
            cursor.execute(raw_query2, [employee_id, company_id, device_id])
    except IntegrityError as e:
        print(f"Error during insertion: {e}")

    return render(request, 'index.html')

def UpdateLog(request): #this funtion will be executed when an employee returns any asset.
    company_id = 1
    device_id = 1
    employee_id = 1
    crr_cond='not fresh'

    raw_query = """
        update assignment_devicelog set returned_condition=%s, returned_date=NOW() where company_id_id=%s and 
        device_id_id=%s and employee_id_id=%s and returned_date is null
    """
    raw_query2 = """
        update assignment_device set device_condition=%s, returned_date=NOW(),occupied=-1 where company_id_id=%s and 
        id=%s
    """

    try:
        # Execute the raw query
        print('ya')
        with connection.cursor() as cursor:
            cursor.execute(raw_query, [crr_cond, company_id, device_id, employee_id])
            cursor.execute(raw_query2, [crr_cond, company_id, device_id])
    except IntegrityError as e:
        print(f"Error during insertion: {e}")

    return render(request, 'index.html')

def seeLog(request): #for viewing all logs of a device
    company_id=1
    device_id=1
    raw_query = 'SELECT * FROM assignment_deviceLog where company_id_id=%s and device_id_id=%s'
    lst = Func.objects.raw(raw_query, [company_id,device_id])
    return render(request,'index.html',{'lst':lst})


