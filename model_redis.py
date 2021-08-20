from model import Model
import pickle
import redis  # type: ignore
import sys
from typing import Dict, List, Tuple


class RedisModel(Model):
    def __init__(self) -> None:
        super().__init__()
        self.client = redis.Redis()
        try:
            self.client.ping()
        except redis.exceptions.ConnectionError as exception:
            print(f'Redis error: {exception}')
            sys.exit(1)

        self.redis_set_objects({})

    def add_object(self, object: str) -> None:
        objects = self.redis_get_objects()
        if object in objects:
            objects[object] += 1
        else:
            objects[object] = 1

        self.redis_set_objects(objects)

    def remove_object(self, object: str) -> None:
        objects = self.redis_get_objects()
        if object in objects and objects[object] > 0:
            objects[object] -= 1

        self.redis_set_objects(objects)

    def get_objects(self) -> List[Tuple[str, int]]:
        objects = self.redis_get_objects()
        return sorted(list((name, num) for name, num in objects.items() if num > 0))

    def redis_set_objects(self, objects: Dict) -> None:
        ret = self.client.set('objects', pickle.dumps(objects))
        assert ret

    def redis_get_objects(self) -> Dict:
        return pickle.loads(self.client.get('objects'))