import pytest
import uuid
from unittest import mock

from  rentomatic.domain.room  import  Room 
from  rentomatic.use_cases.room_list  import  room_list_use_case 
from rentomatic.requests.room_list import RoomListRequest



@pytest.fixture
def domain_rooms():
    room_1 = Room(
       code=uuid.uuid4(),
       size=215,
       price=39,
       longitude=-0.09998975,
       latitude=51.75436293
    )

    room_2 = Room(
       code=uuid.uuid4(),
       size=405,
       price=66,
       longitude=-0.09998975,
       latitude=51.75436293
    )

    room_3 = Room(
       code=uuid.uuid4(),
       size=56,
       price=60,
       longitude=-0.09998975,
       latitude=51.75436293
    )

    room_4 = Room(
       code=uuid.uuid4(),
       size=93,
       price=48,
       longitude=-0.09998975,
       latitude=51.75436293
    )

    return [room_1, room_2, room_3, room_4]

def test_list_rooms_without_params(domain_rooms):
   repo = mock.Mock()
   repo.list.return_value = domain_rooms
   
   request = RoomListRequest()

   response = room_list_use_case(repo, request)

   assert bool(response) is True
   
   # Check is that the repository method was called without any params.
   repo.list.assert_called_with()

   assert response.value == domain_rooms