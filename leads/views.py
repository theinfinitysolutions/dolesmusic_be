import datetime
import requests
import logging  # Import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeadSerializer, BusinessLeadSerializer
from django.conf import settings

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class CreateLeadView(APIView):
    def post(self, request):
        logging.debug("Received POST request with data: %s", request.data)
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            logging.debug("Serializer is valid. Data: %s", serializer.validated_data)

           

            # Function to refresh access token
            def refresh_access_token():
                url = "https://accounts.zoho.in/oauth/v2/token"
                params = {
                    "refresh_token": settings.ZOHO_REFRESH_TOKEN,
                    "client_id": settings.ZOHO_CLIENT_ID,
                    "client_secret": settings.ZOHO_CLIENT_SECRET,
                    "grant_type": "refresh_token"
                }
             
                response = requests.post(url, params=params)
                return response

            # Attempt to get access token
            
            response = refresh_access_token()

            access_token = response.json().get("access_token")
            print(access_token)
            if not access_token:
                logging.error("Failed to obtain access token: %s", response.json())
                return Response(
                    {"message": "Failed to obtain access token", "error": response.json()},
                    status=status.HTTP_400_BAD_REQUEST
                )

           

            # Data from the client
            data = serializer.validated_data

            # Zoho CRM API Endpoint
            url = "https://www.zohoapis.in/crm/v2/Leads"

            # Headers and Payload
            headers = {
                "Authorization": f"Zoho-oauthtoken {access_token}",
                "Content-Type": "application/json",
            }
            payload = {
                "data": [
                    {
                        "Name1": f"{data['first_name']} {data['last_name']}",
                        "Email": data['email'],
                        "Phone": data.get('phone', ''),
                        "Purposes": [data.get('purpose', '')],
                        "Budget": f"₹{data.get('budget', '')}",
                        "Message": data.get('message', ''),
                        "Created_On": datetime.datetime.now().strftime("%Y-%m-%d"),
                        "Preferred_Time_Slot1": [data.get('time_slot', '')],
                        "Experience_Level": [data.get('experience', '')],
                        "Country": data.get('country', ''),
                        "State": data.get('state', ''),
                        "Campaign": data.get('campaign', ''),
                        "AdSet": data.get('adset', ''),
                        "Placement": data.get('placement', ''),
                        "Ad_Id": data.get('ad', ''),
                        "Last_Name": data.get('last_name', ''),
                        "Tags": data.get('artist_name', '')
                    }
                ]
            }

            print(payload)

            response = requests.post(url, json=payload, headers=headers)
            logging.debug("Response from Zoho (lead creation request): %s", response.json())

            if response.status_code == 201:
                logging.info("Lead created successfully")
                return Response(
                    {"message": "Lead created successfully", "data": response.json()},
                    status=status.HTTP_201_CREATED,
                )
            else:
                logging.error("Failed to create lead: %s", response.json())
                return Response(
                    {
                        "message": "Failed to create lead",
                        "error": response.json(),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            logging.error("Serializer errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateBusinessLeadView(APIView):
    def post(self, request):
        logging.debug("Received POST request with data: %s", request.data)
        serializer = BusinessLeadSerializer(data=request.data)
        if serializer.is_valid():
            

            # Function to refresh access token
            def refresh_access_token():
                url = "https://accounts.zoho.in/oauth/v2/token"
                params = {
                    "refresh_token": settings.ZOHO_REFRESH_TOKEN,
                    "client_id": settings.ZOHO_CLIENT_ID,
                    "client_secret": settings.ZOHO_CLIENT_SECRET,
                    "grant_type": "refresh_token"
                }
             
                response = requests.post(url, params=params)
                return response

            # Attempt to get access token
            
            response = refresh_access_token()

            access_token = response.json().get("access_token")
            print(access_token)
            if not access_token:
                logging.error("Failed to obtain access token: %s", response.json())
                return Response(
                    {"message": "Failed to obtain access token", "error": response.json()},
                    status=status.HTTP_400_BAD_REQUEST
            )

            data = serializer.validated_data
            # Get an access token for Zoho CRM
            if not access_token:
                logging.error("Failed to get Zoho access token")
                return Response(
                    {"message": "Failed to authenticate with Zoho CRM"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            # Create lead in Zoho CRM
            url = "https://www.zohoapis.in/crm/v2/Business_Leads"
            headers = {
                "Authorization": f"Zoho-oauthtoken {access_token}",
                "Content-Type": "application/json",
            }
            payload = {
                "data": [
                    {
                        "Name": data.get('company_name', ''),
                        "Email": data['email'],
                        "Last_Name": data['last_name'],
                        "First_Name": data['first_name'],
                        "Message": data.get('message', ''),
                        "Designation": data.get('designation', '')
                    }
                ]
            }

            print(payload)

            response = requests.post(url, json=payload, headers=headers)
            logging.debug("Response from Zoho (lead creation request): %s", response.json())

            if response.status_code == 201:
                logging.info("Lead created successfully")
                return Response(
                    {"message": "Lead created successfully", "data": response.json()},
                    status=status.HTTP_201_CREATED,
                )
            else:
                logging.error("Failed to create lead: %s", response.json())
                return Response(
                    {
                        "message": "Failed to create lead",
                        "error": response.json(),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            logging.error("Serializer errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
