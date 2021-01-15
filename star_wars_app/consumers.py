import json
from channels.generic.websocket import AsyncWebsocketConsumer
from star_wars_app import altagram

class StarShipConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "starwar"
        print("connecting")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        ship = json.loads(text_data)
        data = {}
        print("ship = ", ship)
        if not ship == "finish":
            wikiPagesId = []
            rating = altagram.getHyperDriveRating(ship, wikiPagesId)
            data[ship] = rating
        else:
            data["status"] = "finish"
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'getShipData',
                'message': json.dumps(data)
            },
        )

    async def getShipData(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
