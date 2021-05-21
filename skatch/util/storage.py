class InMemoryStorage:
    __instance = None

    def __init__(self):
        self.room_data = dict()
        self.user_data = dict()

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def join_user(self, user_id, room_id, user_info):
        self.room_data[room_id]['users'][user_id] = {
            'score': 0,
            'nickname': user_info['nickname'],
            'character': user_info['character']
        }


storage = InMemoryStorage.instance()

"""
{
	room_id: {
		'round': int,
		'problem': str,
		'host': int
		'paint': ???(ask to SH),
		'remaining_time': int,
		'status': Enum,
		'is_public': bool,
		'users': {
			session_id: {
				'score': int,
				'nickname: str,
				'character': str
			}
		}
		'correct_users': [session_id],
		'drawer': session_id
	}
}
"""
