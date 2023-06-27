""""
Copyright © AverseABFun/sdft 2023 - https://github.com/AverseABFun-Windows
Description:
A discord text adventure bot

Version: 0.0.1
"""
import json

def get_room_data(location: str):
    try:
        room_file = open(f"rooms/{location}.json",'r').read()
    except:
        raise ValueError(f"Location {location} is an invalid location")
    room = json.loads(room_file)
    return room