from rest_framework.serializers import ModelSerializer, SerializerMethodField
from main.models import *


class TeamsSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class UsersTeamsPKSerializer(ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ['id', 'role']
        read_only_fields = ['id', 'role']


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class TeamMembersSerializer(ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class TeamProjectsSerializer(ModelSerializer):
    class Meta:
        model = TeamProjects
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class SectionsSerializer(ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class ElementsSerializer(ModelSerializer):

    class Meta:
        model = Elements
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class ElementsItemsSerializer(ModelSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Elements
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'items']

    def get_items(self, obj):
        queryset = Items.objects.filter(element=obj.id)
        serialized = ItemsSerializer(queryset, many=True)
        return serialized.data


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectMembersSerializer(ModelSerializer):
    class Meta:
        model = ProjectMembers
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


# Helping serializer
class UsersTeamsSerializer(ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ['team']
        depth = 1


# Helping serializer
class ProjectsNameSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name']


# Helping serializer
class TeamsProjectsSerializer(ModelSerializer):
    class Meta:
        model = TeamProjects
        fields = ['project']
        depth = 1


# Helping serializer
class UsersProjectsSerializer(ModelSerializer):
    class Meta:
        model = ProjectMembers
        fields = ['project']
        depth = 1


class ElementsTitleSerializer(ModelSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Elements
        fields = ['id', 'title']

class CategoryElementsSerializer(ModelSerializer):
    elements = SerializerMethodField()

    class Meta:
        model = Categories
        fields = ['id', 'name', 'description', 'order', 'elements']

    def get_elements(self, obj):
        queryset = Elements.objects.filter(category=obj.id)
        serialized = ElementsSerializer(queryset, many=True)
        return serialized.data
