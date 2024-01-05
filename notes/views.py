# notes/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Note
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # Retrieve the username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate the username and password
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = User.objects.filter(username=username).first()
        print(f"USer: {user}. Password: {user.password}")

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        # If authentication is successful, generate and return an access token
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class NoteListView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print("DELETE ME NOTES", Note.objects.filter(owner=self.request.user))
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


class CreateNoteView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpdateNoteView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


class DeleteNoteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


class ShareNoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, owner=request.user)
        shared_user_id = request.data.get('user_id')
        shared_user = get_object_or_404(User, pk=shared_user_id)
        
        # Perform sharing logic, e.g., add the shared_user to the shared_with field of the note
        note.shared_with.add(shared_user)
        
        return Response({'message': 'Note shared successfully'}, status=status.HTTP_200_OK)


class SearchNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q', '')
        
        notes = Note.objects.filter(owner=request.user, title__icontains=query)
        serializer = NoteSerializer(notes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
