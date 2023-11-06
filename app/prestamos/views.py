from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PruebaAPI(APIView):

    permission_classes = [IsAuthenticated,]
    
    def get(self,request):
        return Response({'content':'Esta vista esta protejida por Dios'})