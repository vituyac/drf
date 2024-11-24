from rest_framework import serializers
import json

class SimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()
    
simple_object = {
    "id": 1,
    "name": "Simple object",
    "description": "This",
    "is_active": True,
}

serializer = SimpleSerializer(data=simple_object)
serializer.is_valid(raise_exception=True) #Если будет ошибка - ошибка высветится

print(serializer.data)
print(json.dumps(serializer.data, ident=4))


#Валидация 
class SimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=2)
    name = serializers.CharField(max_lenght=100)
    description = serializers.CharField(max_lenght=1000, required=False) #required - обязательный?
    is_active = serializers.BooleanField(default=True)
    
data = {
    "id": 1,
    "name": "Simple object",
    "description": "This",
    "is_active": True,
}

serializer = SimpleSerializer(data=data)
serializer.is_valid(raise_exception=True)

#Кастомная валидация
class SimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=2)
    name = serializers.CharField(max_lenght=100)
    description = serializers.CharField(max_lenght=1000, required=False) #required - обязательный?
    is_active = serializers.BooleanField(default=True)
    
    def validate_name(self, value):
        if "simple" not in value.lower():
            raise serializers.ValidationError("Error")
        return value
    
#На уровне объекта
class SimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=2)
    name = serializers.CharField(max_lenght=100)
    description = serializers.CharField(max_lenght=1000, required=False) #required - обязательный?
    another_description = serializers.CharField(max_lenght=1000, required=False)
    is_active = serializers.BooleanField(default=True)
    
    def validate(self, data):
        if data["description"] == data["another_description"]:
            raise serializers.ValidationError("Error")
        return data
    
    
#Связанные объекты
class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_lenght=100) #read_only=True только на вывод
    
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_lenght=100)
    author = AuthorSerializer() #если несколько авторов то many=True
    
author_data = {
    "id": 1,
    "name": "Author",
}

author_data = {
    "id": 1,
    "name": "Book",
    "author": {
        "id": 1,
        "name": "Author",
    },
}

#Собственные поля
class YesNoField(serializers.BooleanField):
    def to_representation(self, value): #наоборот
        return "Yes" if value else "No"
    
    def to_internal_value(self, data): #из json в питон
        if isinstance(data, bool):
            return data
        if data.lower() == "yes":
            return True
    
class SimpleSerializer(serializers.Serializer):
    is_active = YesNoField()
    
#На сериалайзеры
class SimpleSerializer(serializers.Serializer):
    is_active = serializers.BooleanField()
    
    def to_representation(self, instance): #из питон в json
        super().to_representation(instance)
    
    def to_internal_value(self, data): #из json в питон
        super().internal_value(data)
        
#Model Serializer
class UserSerializer(serializers.ModelSerializer):
    
    combo_name = serializers.SerializerMethodField()
    
    def get_combo_name(self, obj):
        return f"{obj['first_name']} {obj['last_name']}"
    
    class Meta:
        model = User
        # fields = "__all__"
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "combo_name",
        )
        
        extra_kwargs = {
            'username': {'required': False},
            'error_messages': {
                'unique': 'Уже существует.'
            }
        }
        
        
    #дополнительный контекст
    class SimpleSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        
        def to_representation(self, instance): #из питон в json
            return {
                "id": instance["id"],
                "name": instance["name"],
                "is_admin": self.context.get("is_admin", False),
            }
            
#Методы save(), create() и update()
#В представлении
#serializer.is_valid(raise_exception=True)
#serializer.save()

def create(self, validated_date):
    return User.objects.create(**validated_data)

def update(self, instance, validated_date):
    instance.title = validated_date.get("title", instance) #и так для всех полей
    instance.save()
    return instance
# def create(self, validated_data):
#         # Удаляем поле, если оно есть
#         validated_data.pop('field_to_remove', None)
#         return User.objects.create(**validated_data)


user = serializers.HiddenField(default=serializers.CurrentUserDefault())