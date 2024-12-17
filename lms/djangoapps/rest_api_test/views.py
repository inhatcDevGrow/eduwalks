from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestModelSerializer
from .models import TestModel
import requests

class TestModelView(APIView):
    def get(self, request):
        url = f"http://local.edly.io/api/courses/v1/courses/course-v1:edX+DemoX+Demo_Course"
        
        response = requests.get(url)
        
        print(response.json())  # API 응답을 출력
        return Response(response.json())  # DRF Response 객체를 반환
        # return Response({
        #     "status": "ok",
        #     "message": "API is working"
        # })



class Get_test_models(APIView):
    def get(self, request):
        test_models = TestModel.objects.all()
        serializer = TestModelSerializer(test_models, many=True)
        print(serializer)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TestModelSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)