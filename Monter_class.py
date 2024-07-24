import random

class Monster:
    def __init__(self):
        self.monsters = {}  # {id: {'level': int, 'name': str, 'path': str}}
        self.object_cards = 0
        self.total_monsters = 12  # 假設總共有12個怪物
        self.default_data = {
            0: {'name': 'Monster0', 'paths': {1: 'path/to/monster0_level1.jpg', 2: 'path/to/monster0_level2.jpg'}},
            1: {'name': 'Monster1', 'paths': {1: 'path/to/monster1_level1.jpg', 2: 'path/to/monster1_level2.jpg'}},
            # 繼續為其他怪物填寫資料
        }

    def addObjectCard(self) -> dict[str, bool | str]:
        self.object_cards += 1
        return {'success': True, 'message': "Object card added"}

    def useObjectCard(self, id: int) -> dict[str, bool | str]:
        if id in self.monsters:
            if self.object_cards > 0:
                self.monsters[id]['level'] += 1
                self.object_cards -= 1
                return {'success': True, 'message': f"Monster {id} upgraded to level {self.monsters[id]['level']}"}
            else:
                return {'success': False, 'message': "No object cards left"}
        else:
            return {'success': False, 'message': "Monster does not exist"}

    def ObjectCardNum(self) -> int:
        return self.object_cards

    def currentMonsterNum(self) -> int:
        return len(self.monsters)

    def allMonsterNum(self) -> int:
        return self.total_monsters

    def MonsterLv(self, id: int) -> int:
        if id in self.monsters:
            return self.monsters[id]['level']
        else:
            return 0

    def getDefaultMonsterName(self, id: int) -> str:
        if 0 <= id < self.total_monsters:
            return self.default_data[id]['name']
        else:
            return "Invalid Monster ID"

    def getMonsterName(self, id: int, level: int | None = None) -> str:
        if id in self.monsters:
            if level is None:
                level = self.monsters[id]['level']
            return f"{self.default_data[id]['name']}_Level{level}"
        else:
            return "Monster does not exist"

    def getMonsterPath(self, id: int, level: int | None = None) -> str:
        if id in self.monsters:
            if level is None:
                level = self.monsters[id]['level']
            return self.default_data[id]['paths'].get(level, "Path not found")
        else:
            return "Monster does not exist"

    def getObjectCardPath(self) -> str:
        return "path/to/object_card.jpg"

    def addMonster(self, id: int | None = None) -> dict[str, bool | str | int]:
        if id is not None:
            if id not in self.monsters and 0 <= id < self.total_monsters:
                self.monsters[id] = {'level': 1, 'name': self.getDefaultMonsterName(id)}
                return {'success': True, 'message': "Monster added", 'id': id}
            else:
                return {'success': False, 'message': "Monster already exists or invalid ID"}
        else:
            available_ids = [i for i in range(self.total_monsters) if i not in self.monsters]
            if available_ids:
                new_id = random.choice(available_ids)
                self.monsters[new_id] = {'level': 1, 'name': self.getDefaultMonsterName(new_id)}
                return {'success': True, 'message': "Monster added", 'id': new_id}
            else:
                return {'success': False, 'message': "All monsters already added"}

# Example usage:
# monster = Monster()
# print(monster.addObjectCard())
# print(monster.useObjectCard(0))
# print(monster.ObjectCardNum())
# print(monster.currentMonsterNum())
# print(monster.allMonsterNum())
# print(monster.MonsterLv(0))
# print(monster.getDefaultMonsterName(0))
# print(monster.getMonsterName(0))
# print(monster.getMonsterName(0, 2))
# print(monster.addMonster(0))
# print(monster.addMonster())
# print(monster.getMonsterPath(0))
# print(monster.getObjectCardPath())
