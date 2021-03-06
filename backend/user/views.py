import random
import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models, serializers

chares = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# for create new user model
@api_view(("POST",))
def signup(request):
    instance = serializers.UserSignUp(data=request.data)
    if instance.is_valid(True):
        instance.save()
        return Response(instance.data, status=status.HTTP_200_OK)


# this can be used for User login
@api_view(("POST",))
def login(request):
    # serialaz passed data
    try:
        username, password = request.data["username"], request.data["password"]
    except KeyError:
        return Response({"msg": "fill necesery field"}, status=status.HTTP_400_BAD_REQUEST)

    # find User instance and authenticated
    try:
        instance = models.User.objects.get(username=username)
        if not instance.password == password:
            raise ValueError
    except (models.User.DoesNotExist, ValueError) as error:
        return Response({'msg': 'username and password is not match'}, status=status.HTTP_401_UNAUTHORIZED)

    # if request reach here every thing is fine and return response with cookies
    data = serializers.UserSignUp(instance)

    response = Response(data, status=status.HTTP_202_ACCEPTED)
    response.set_cookie('moritoken', new_mori_token(instance))
    return response


# this method use for frontend for not display inside app
# but client still can send request to another apis but apis are secure with is_authenticated()
@api_view(("GET",))
def is_authenticated_api(request):
    user = is_authenticated(request)
    if type(user) is Response:
        return Response({"msg": "plz authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"msg": "ok"}, status=status.HTTP_200_OK)


def new_mori_token(user):
    # find and delete old token if exsit
    try:
        exist_token = models.MoriToken.objects.get(user=user)
        exist_token.delete()
    except models.MoriToken.DoesNotExist:
        pass

    # generete new token
    token = ''
    for _ in range(25):
        token += random.choice(chares)

    # create new mori_token and return token
    models.MoriToken.objects.create(token=token, user=user)
    return token


# this method use in backend when we want response data related to a user
def is_authenticated(request):
    time_now = datetime.datetime.now()

    # get cookie
    try:
        token = request.COOKIES["moritoken"]
    except KeyError:
        return Response({"error": "you are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    # get token with existing cookie
    try:
        moritoken = models.MoriToken.objects.get(token=token)
    except models.MoriToken.DoesNotExist:
        return Response({"error": "you are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    # chech if token is not expiration
    if datetime.timedelta(minutes=30) < time_now - moritoken.created.replace(tzinfo=None):
        moritoken.delete()
        return Response({"error": "is been to long from last request login again"}, status=status.HTTP_401_UNAUTHORIZED)

    # if request rach here everything is all right
    moritoken.created = time_now
    moritoken.save()
    return moritoken.user
