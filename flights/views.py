from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from flights.models import Schedule
from flights.serializers import UserSerializer, ScheduleSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#APIS
# /flights/

@csrf_exempt
def flight_list(request):
    #Get all
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        schedules_serializer = ScheduleSerializer(schedules,many=True)
        print(schedules_serializer.data)
        return JsonResponse(schedules_serializer.data, safe=False)
    
    #Add one
    if request.method == 'POST':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Delete All
    if request.method == 'DELETE':
        Schedule.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    

@csrf_exempt
def flight_detail(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    #Retrive one record
    if request.method == 'GET':
        schedule_serializer = ScheduleSerializer(schedule)
        print(schedule_serializer.data)
        return JsonResponse(schedule_serializer.data,safe=False)

    #Update one record
    if request.method == 'PUT':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(schedule, data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data,safe=False)  
        return JsonResponse(schedule_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #Delete one record
    if request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def reset(request):
    jsonData = [
        {
            "id": 1,
            "airline": "United Airlines",
            "flight_no": "UA1234",
            "trip_type": "Round Trip",
            "departure_airport": "ORD",
            "arrival_airport": "LAX",
            "departure_date": "2019-06-24",
            "return_date": "2019-06-25"
        },
        {
            "id": 2,
            "airline": "American Airlines",
            "flight_no": "AA1952",
            "trip_type": "One Way",
            "departure_airport": "LAX",
            "arrival_airport": "ABQ",
            "departure_date": "2019-06-25",
            "return_date": "2019-06-26"
        },
        {
            "id": 3,
            "airline": "Southwest Airlines",
            "flight_no": "WN4307",
            "trip_type": "Round Trip",
            "departure_airport": "ORD",
            "arrival_airport": "DEN",
            "departure_date": "2019-06-25",
            "return_date": "2019-06-26"
        },
        {
            "id": 4,
            "airline": "Alaska Airlines",
            "flight_no": "AS1677",
            "trip_type": "One Way",
            "departure_airport": "BOS",
            "arrival_airport": "CLT",
            "departure_date": "2019-06-27",
            "return_date": "2019-06-28"
        },
        {
            "id": 5,
            "airline": "Hawaiian Airlines",
            "flight_no": "HA4233",
            "trip_type": "Round Trip",
            "departure_airport": "HNL",
            "arrival_airport": "LAX",
            "departure_date": "2019-06-28",
            "return_date": "2019-06-29"
        },
        {
            "id": 6,
            "airline": "Virgin Atlantic",
            "flight_no": "VS1980",
            "trip_type": "Round Trip",
            "departure_airport": "SEA",
            "arrival_airport": "LHR",
            "departure_date": "2019-06-29",
            "return_date": "2019-07-02"
        },
        {
            "id": 7,
            "airline": "Korean Air",
            "flight_no": "KE5233",
            "trip_type": "One Way",
            "departure_airport": "ORD",
            "arrival_airport": "ICN",
            "departure_date": "2019-06-28",
            "return_date": "2019-07-02"
        },
        {
            "id": 8,
            "airline": "Delta Air Lines",
            "flight_no": "DL1889",
            "trip_type": "One Way",
            "departure_airport": "MIA",
            "arrival_airport": "ORD",
            "departure_date": "2019-07-01",
            "return_date": "2019-07-02"
        },
        {
            "id": 9,
            "airline": "Malasia Airlines",
            "flight_no": "MH9880",
            "trip_type": "Round Trip",
            "departure_airport": "JFK",
            "arrival_airport": "KUL",
            "departure_date": "2019-06-29",
            "return_date": "2019-07-03"
        },
        {
            "id": 10,
            "airline": "Air New Zealand",
            "flight_no": "NZ8029",
            "trip_type": "One Way",
            "departure_airport": "DEN",
            "arrival_airport": "ALR",
            "departure_date": "2019-06-28",
            "return_date": "2019-07-02"
        }
    ]
    message = "Table is not empty."
    schedules = Schedule.objects.all()
    if(not schedules):
        for item in jsonData:       
            schedule_serializer = ScheduleSerializer(data=item)
            if schedule_serializer.is_valid():
                schedule_serializer.save()
        message = "Done!"     
    return HttpResponse("<h1>"+message+"</h1>")          

@csrf_exempt
def purge(request):
    Schedule.objects.all().delete()
    return HttpResponse("<h1>All Deleted!</h1>")    