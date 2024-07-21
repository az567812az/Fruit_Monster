class Monster:
    def __init__(self):
        self.monsters = {}  # Dictionary to store monster info: {id: {'level': int, 'name': str}}
        self.object_cards = 0
        self.total_monsters = 15    # There have 15 fruit monster
                                    #1: cucumber
                                    #2: apple
                                    #3: kiwi
                                    #4: banana
                                    #5: orange
                                    #6: coconut
                                    #7: peach
                                    #8: cherry
                                    #9: pear
                                    #10: pomegranate
                                    #11: pineapple 
                                    #12: watermelon
                                    #13: melon
                                    #14: grape
                                    #15: strawberry

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
        if 1 <= id <= self.total_monsters:
            return f"MonsterDefaultName{id}"
        else:
            return "Invalid Monster ID"

    def getMonsterName(self, id: int, level: int | None = None) -> str:
        if id in self.monsters:
            if level is None:
                level = self.monsters[id]['level']
            return f"MonsterName{id}_Level{level}"
        else:
            return "Monster does not exist"

    def addMonster(self, id: int | None = None) -> dict[str, bool | str | int]:
        if id is not None:
            if id not in self.monsters and 1 <= id <= self.total_monsters:
                self.monsters[id] = {'level': 1, 'name': self.getDefaultMonsterName(id)}
                return {'success': True, 'message': "Monster added", 'id': id}
            else:
                return {'success': False, 'message': "Monster already exists or invalid ID"}
        else:
            for new_id in range(1, self.total_monsters + 1):
                if new_id not in self.monsters:
                    self.monsters[new_id] = {'level': 1, 'name': self.getDefaultMonsterName(new_id)}
                    return {'success': True, 'message': "Monster added", 'id': new_id}
            return {'success': False, 'message': "All monsters already added"}

# Example usage:
# monster = Monster()
# print(monster.addObjectCard())
# print(monster.useObjectCard(1))
# print(monster.ObjectCardNum())
# print(monster.currentMonsterNum())
# print(monster.allMonsterNum())
# print(monster.MonsterLv(1))
# print(monster.getDefaultMonsterName(1))
# print(monster.getMonsterName(1))
# print(monster.getMonsterName(1, 2))
# print(monster.addMonster(1))
# print(monster.addMonster())
