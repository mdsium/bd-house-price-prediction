from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import HousePredictionSerializer
from .utils import predict_house_price

from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import ContactMessageSerializer
from .models import ContactMessage

from .models import HousePrediction   # ← Import করো


class PredictPriceAPIView(APIView):
    @swagger_auto_schema(request_body=HousePredictionSerializer)
    def post(self, request):
        serializer = HousePredictionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                price = predict_house_price(serializer.validated_data)
                return Response({
                    "predicted_price": price,
                    "formatted_price": f"{price:,} BDT"
                })
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        return Response(serializer.errors, status=400)



class ContactFormAPIView(APIView):
    @swagger_auto_schema(request_body=ContactMessageSerializer)
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Inquiry received successfully! We will contact you soon.",
                "status": "success"
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PredictPriceAPIView(APIView):
    @swagger_auto_schema(request_body=HousePredictionSerializer)
    def post(self, request):
        serializer = HousePredictionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Price Predict করো
                price = predict_house_price(serializer.validated_data)
                formatted = f"{price:,} BDT"

                # ✅ Database-এ সেভ করো
                HousePrediction.objects.create(
                    **serializer.validated_data,
                    predicted_price=price,
                    formatted_price=formatted
                )

                return Response({
                    "predicted_price": price,
                    "formatted_price": formatted,
                    "message": "Prediction saved successfully"
                })
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        
        return Response(serializer.errors, status=400)


class PredictionHistoryAPIView(APIView):
    def get(self, request):
        predictions = HousePrediction.objects.all()[:50]  # Last 50 predictions
        data = []
        for p in predictions:
            data.append({
                "id": p.id,
                "created_at": p.created_at.strftime("%Y-%m-%d %H:%M"),
                "city": p.city,
                "thana": p.thana,
                "area_sqft": p.area_sqft,
                "bedrooms": p.bedrooms,
                "predicted_price": p.predicted_price,
                "formatted_price": p.formatted_price,
            })
        return Response(data)