from main.models import News, Place, Task, Schedule
from main.models import Skill, Hobby, TypeImportance, TypeEvent, Events
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

    def create(self, validated_data):
        return Skill.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('pk', 'name', 'description', "skills")

    def create(self, validated_data):
        hobby = Hobby.objects.create(name=validated_data.get('name'),
                                     description=validated_data.get('description'))
        if 'skills' in validated_data:
            hobby.skills.add(*validated_data['skills'])
        return hobby

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        if 'skills' in validated_data:
            instance.skills.add(*validated_data['skills'])
        instance.save()
        return instance

    def delete_skills(self, skills):
        for skill in skills:
            self.instance.skills.remove(Skill.objects.filter(pk=skill).first())
        return self.instance


class HobbyReadSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Hobby
        fields = "__all__"


class TypeImportanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeImportance
        fields = '__all__'

    def create(self, validated_data):
        return TypeImportance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.importance = validated_data.get('importance', instance.importance)
        instance.save()
        return instance


class TypeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEvent
        fields = '__all__'

    def create(self, validated_data):
        return TypeEvent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

    def create(self, validated_data):
        event = Events.objects.create(name=validated_data['name'],
                                      description=validated_data.get('description'),
                                      start_date=validated_data.get('start_date'),
                                      end_date=validated_data.get('end_date'),
                                      social_link=validated_data.get('social_link'),
                                      )
        if 'hobbies' in validated_data:
            event.hobbies.add(*validated_data['hobbies'])
        if 'skills' in validated_data:
            event.skills.add(*validated_data['skills'])
        event.type_importance = validated_data.get('type_importance')
        event.type_event = validated_data.get('type_event')
        event.save()
        return event

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.social_link = validated_data.get('social_link', instance.social_link)
        if 'hobbies' in validated_data:
            instance.hobbies.add(*validated_data['hobbies'])
        if 'skills' in validated_data:
            instance.skills.add(*validated_data['skills'])
        instance.type_importance = validated_data.get('type_importance', instance.type_importance)
        instance.type_event = validated_data.get('type_event', instance.type_event)
        instance.save()
        return instance


class EventReadSerializer(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    type_importance = TypeImportanceSerializer(allow_null=False)
    type_event = TypeEventSerializer(allow_null=True)

    class Meta:
        model = Events
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def create(self, validated_data):
        news = News.objects.create(name=validated_data.get('name'),
                                   description=validated_data.get('description'))
        if 'hobbies' in validated_data:
            news.hobbies.add(*validated_data['hobbies'])
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        if 'hobbies' in validated_data:
            instance.hobbies.add(*validated_data['hobbies'])
        instance.save()
        return instance


class NewsReadSerializer(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def create(self, validated_data):
        place = Place.objects.create(**validated_data)
        place.save()
        return place

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.type_integer = validated_data.get('type_integer', instance.type_integer)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.type_integer = validated_data.get('type_integer', instance.type_integer)
        instance.subject_integer = validated_data.get('subject_integer', instance.subject_integer)
        instance.save()
        return instance


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        schedule = Schedule.objects.create(**validated_data)
        schedule.save()
        return schedule

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.type_integer = validated_data.get('type_integer', instance)
        instance.type_integer_id = validated_data.get('type_integer_id', instance.type_integer_id)
        instance.save()
        return instance
