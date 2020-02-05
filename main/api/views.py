from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from main.models import *
from main.api.serializers import *
from users.api.authentication import UserAuthentication

class TeamsViewSet(ViewSet):
    def list(self, request):

        # print('request', request.loged_in_user)
        queryset = Teams.objects.all()
        serializer = TeamsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Teams.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        serializer = TeamsSerializer(team)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = TeamsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            data = {
                "user": request.user.id,
                "team": Teams.objects.last().id,
                "role": 1
            }
            team_member = TeamMembersSerializer(data=data)
            if team_member.is_valid():
                team_member.save()

            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Teams.objects.get(pk=pk)
        data = request.data
        serialized = TeamsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Teams.objects.get(pk=pk)
        data = request.data
        serialized = TeamsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        team = Teams.objects.get(pk=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RolesViewSet(ViewSet):
    def list(self, request):
        queryset = Roles.objects.all()
        serializer = RolesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Roles.objects.all()
        role = get_object_or_404(queryset, pk=pk)
        serializer = RolesSerializer(role)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = RolesSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Roles.objects.get(pk=pk)
        data = request.data
        serialized = RolesSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Roles.objects.get(pk=pk)
        data = request.data
        serialized = RolesSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        role = Roles.objects.get(pk=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamMembersViewSet(ViewSet):
    def list(self, request):
        queryset = TeamMembers.objects.all()
        serializer = TeamMembersSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TeamMembers.objects.all()
        team_member = get_object_or_404(queryset, pk=pk)
        serializer = TeamMembersSerializer(team_member)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = TeamMembersSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = TeamMembers.objects.get(pk=pk)
        data = request.data
        serialized = TeamMembersSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = TeamMembers.objects.get(pk=pk)
        data = request.data
        serialized = TeamMembersSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        team_member = TeamMembers.objects.get(pk=pk)
        team_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectsViewSet(ViewSet):
    def list(self, request):
        queryset = Projects.objects.all()
        serializer = ProjectsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Projects.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectsSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = ProjectsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Projects.objects.get(pk=pk)
        data = request.data
        serialized = ProjectsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Projects.objects.get(pk=pk)
        data = request.data
        serialized = ProjectsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        project = Projects.objects.get(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamProjectsViewSet(ViewSet):
    def list(self, request):
        queryset = TeamProjects.objects.all()
        serializer = TeamProjectsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TeamProjects.objects.all()
        team_project = get_object_or_404(queryset, pk=pk)
        serializer = TeamProjectsSerializer(team_project)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = TeamProjectsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = TeamProjects.objects.get(pk=pk)
        data = request.data
        serialized = TeamProjectsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = TeamProjects.objects.get(pk=pk)
        data = request.data
        serialized = TeamProjectsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        team_project = TeamProjects.objects.get(pk=pk)
        team_project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SectionsViewSet(ViewSet):
    def list(self, request):
        queryset = Sections.objects.all()
        serializer = SectionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sections.objects.all()
        section = get_object_or_404(queryset, pk=pk)
        serializer = SectionsSerializer(section)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = SectionsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Sections.objects.get(pk=pk)
        data = request.data
        serialized = SectionsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Sections.objects.get(pk=pk)
        data = request.data
        serialized = SectionsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        section = Sections.objects.get(pk=pk)
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriesViewSet(ViewSet):
    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Categories.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = CategoriesSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Categories.objects.get(pk=pk)
        data = request.data
        serialized = CategoriesSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Categories.objects.get(pk=pk)
        data = request.data
        serialized = CategoriesSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        category = Categories.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ElementsViewSet(ViewSet):
    def list(self, request):
        queryset = Elements.objects.all()
        serializer = ElementsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Elements.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = ElementsSerializer(element)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = ElementsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Elements.objects.get(pk=pk)
        data = request.data
        serialized = ElementsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Elements.objects.get(pk=pk)
        data = request.data
        serialized = ElementsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        element = Elements.objects.get(pk=pk)
        element.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemsViewSet(ViewSet):
    def list(self, request):
        queryset = Items.objects.all()
        serializer = ItemsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Items.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = ItemsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Items.objects.get(pk=pk)
        data = request.data
        serialized = ItemsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Items.objects.get(pk=pk)
        data = request.data
        serialized = ItemsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        item = Items.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentsViewSet(ViewSet):
    def list(self, request):
        queryset = Comments.objects.all()
        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comments.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def create(self, request):
        data=request.data
        serialized = CommentsSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def update(self, request, pk=None):
        inst = Comments.objects.get(pk=pk)
        data = request.data
        serialized = CommentsSerializer(instance=inst, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def partial_update(self, request, pk=None):
        inst = Comments.objects.get(pk=pk)
        data = request.data
        serialized = CommentsSerializer(instance=inst, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=201)

    def destroy(self, request, pk=None):
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsersTeamsView(ViewSet):
    def list(self, request):
        # token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        # print("asd",token)
        # user=UserAuthentication()
        # print(user)
        print('user.id', request.user.id)
        print('user teams', request.user_meta['teams'])
        queryset = TeamMembers.objects.filter(user_id=request.user.id)
        serializer = UsersTeamsSerializer(queryset, many=True)
        return Response(serializer.data)