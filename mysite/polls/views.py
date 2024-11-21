from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import permission_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
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


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_update(request, pk):

    try:
        person = Person.objects.get(pk=pk)

    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(person, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def person_delete(request, pk):

    try:
        person = Person.objects.get(pk=pk)

    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def osoba_list(request):

    if request.method == 'GET':

        nazwa = request.query_params.get('nazwa', None)

        if request.user.has_perm('yourapp.can_view_other_persons'):
            queryset = Osoba.objects.all()

        else:
            queryset = Osoba.objects.filter(wlasciciel=request.user)

        if nazwa:
            queryset = queryset.filter(nazwisko__icontains=nazwa)

        serializer = OsobaSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        if not request.user.has_perm('polls.add_osoba'):
            raise PermissionDenied()

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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_members(request, id):

    try:
        stanowisko = Stanowisko.objects.get(pk=id)
        osoby = Osoba.objects.filter(stanowisko=stanowisko)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    except Stanowisko.DoesNotExist:
        return Response(
            {
                "error": "Stanowisko nie istnieje"
            },
            status=status.HTTP_404_NOT_FOUND)
