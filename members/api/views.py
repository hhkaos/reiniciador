from rest_framework import generics

from ..models import Member
from .serializers import UserSerializer, GroupSerializer, MemberSerializer

class MemberList(generics.ListAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    model = Member

    '''def get_queryset(self):
        args = self.get_context_data(**kwargs)
        import ipdb; ipdb.set_trace()

        return Member.objects.filter(user__username = args["username"])'''


class MemberDetail(generics.RetrieveUpdateAPIView):
    #import ipdb; ipdb.set_trace()
    #queryset = Member.objects.get(user__username='hhkaos')
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    model = Member
