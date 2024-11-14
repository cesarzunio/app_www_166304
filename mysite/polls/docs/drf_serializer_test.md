from polls.serializers import TeamSerializer, PersonSerializer
from polls.models import Team, Person

team_data = {'name': 'FC Barcelona', 'country': 'ES'}
serializer = TeamSerializer(data=team_data)

if serializer.is_valid():
    team = serializer.save()
    print(team.name)

team = Team.objects.first()
serializer = TeamSerializer(team)
print(serializer.data)

person_data = {
    'name': 'Jan',
    'surname': 'Kowalski',
    'shirt_size': 'M',
    'month_added': 1,
}

serializer = PersonSerializer(data=person_data)

if serializer.is_valid():
    person = serializer.save()
    print(f"{person.name} {person.surname}")

person = Person.objects.first()
serializer = PersonSerializer(person)
print(serializer.data)
