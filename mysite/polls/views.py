from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Stanowisko, Person, Team
from .serializers import OsobaSerializer, StanowiskoSerializer, PersonSerializer


def index(request):
    return HttpResponse("Helou world!")


@api_view(['GET'])
def person_list(request):

    if request.method == 'GET':

        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def person_detail(request, pk):

    try:
        person = Person.objects.get(pk=pk)

    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_update_delete(request, pk):

    try:
        person = Person.objects.get(pk=pk)

    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

        serializer = PersonSerializer(person, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def osoba_list(request):

    if request.method == 'GET':

        nazwa = request.query_params.get('nazwa', None)

        if nazwa:

            osoby = Osoba.objects.filter(
                nazwisko__icontains=nazwa,
                wlasciciel=request.user)

        else:
            osoby = Osoba.objects.filter(wlasciciel=request.user)

        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = OsobaSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(wlasciciel=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def osoba_detail(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk, wlasciciel=request.user)

    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'DELETE':

        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def stanowisko_list(request):

    if request.method == 'GET':

        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = StanowiskoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def stanowisko_detail(request, pk):

    try:
        stanowisko = Stanowisko.objects.get(pk=pk)

    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'DELETE':

        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)