from django.shortcuts import render

# Create your views here.
from util.storage import InMemoryStorage, storage


def join(): "asdfasdf/asdfasdf"
    user_id = req.~~
    room_id = ~~
    user_info = {
        'character':req.~,
        'nickname': req.~~
    }
    storage.join_user(user_id,room_id,user_info)