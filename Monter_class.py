class Monster:
    def __init__(self):
        self.monsters = {}  # Dictionary to store monster info: {id: {'level': int, 'name': str}}
        self.object_cards = 0
        self.total_monsters = 15    # There have 15 fruit monster
                                    #0: cucumber
                                    #1: apple
                                    #2: kiwi
                                    #3: banana
                                    #4: orange
                                    #5: coconut
                                    #6: peach
                                    #7: cherry
                                    #8: pear
                                    #9: pomegranate
                                    #10: pineapple 
                                    #11: watermelon
                                    #12: melon
                                    #13: grape
                                    #14: strawberry
        self.monstersDB = {
            0: {'Default name': 'cucumber', 'levels': [
                {'name': 'cucumber basic', 'img_pth': '/img/to/cucumberbasic'}, 
                {'name': 'cucumber adv', 'img_pth': '/img/to/cucumberadv'}]
            },
            1: {'Default name': 'cucumber', 'levels': [
                {'name': 'cucumber basic', 'img_pth': '/img/to/cucumberbasic'}, 
                {'name': 'cucumber adv', 'img_pth': '/img/to/cucumberadv'}]
            }
        }

    def getPath(self, id: int, level: int | None = None) -> str:  # get path of current monster pic (of current or specific level)
        if level is not None:
            return self.monstersDB[id]['levels'][self.monsters[id]['level']]

    def allMonsterNums(self) -> int:  # Total number of monsters
        return self.total_monsters
    
    def MonsterNum(self) -> int:  # Number of monsters currently held
        return len(self.monsters)
    
    def exist(self, id: int) -> bool:  # Whether that monster is currently held
        return id in self.monsters
    
    def MonsterLv(self, id: int) -> int:  # Get the current level of the monster
        if id in self.monsters:
            return self.monsters[id]['level']
        else:
            return 0
    
    def addMonster(self, id: int | None = None) -> dict[str, bool | str] | dict[str, bool | str | int]:
        if id is not None:  # random select a monster (don't repeat), returns success=False if no monster left to add. If added monster, also return the id of the added monster.
            if id not in self.monsters and 1 <= id <= self.total_monsters:
                self.monsters[id] = {'level': 1, 'name': self.getDefaultMonsterName(id)}
                return {'success': True, 'message': "Monster added"}
            else:  # add the monster, returns success=False if monster with id already exists
                return {'success': False, 'message': "Monster already exists or invalid ID"}
        else:
            for new_id in range(1, self.total_monsters + 1):
                if new_id not in self.monsters:
                    self.monsters[new_id] = {'level': 1, 'name': self.getDefaultMonsterName(new_id)}
                    return {'success': True, 'message': "Monster added", 'id': new_id}
            return {'success': False, 'message': "All monsters already added"}
    
    def getDefaultMonsterName(self, id: int) -> str:  # Get the default name of the monster
        if 1 <= id <= self.total_monsters:
            return f"MonsterDefaultName{id}"
        else:
            return "Invalid Monster ID"
    
    def getMonsterName(self, id: int, level: int | None = None) -> str:
        if id in self.monsters:
            if level is None:  # Get the name of the monster at the current level
                if level is None:
                    level = self.monsters[id]['level']
                    return f"MonsterName{id}_Level{level}"
            else:  # Get the name of the monster at the specified level
                return "MonsterName of level _"
        else:
            return "Monster does not exist"
    
    def ObjectCardNum(self) -> int:  # get the numbers of object cards currentlt held
        return self.object_cards
    
    def addObjectCard(self) -> dict[str, bool | str]:   # add a object card
        self.object_cards += 1
        return {'success': True, 'message': "Object card added"}

    def upgrade(self, id: int) -> dict[str, bool | str]:  # use a object card on a monster. success=False if monster doesn't exist or can't upgrade anymore or no card available to upgrade.
        if id in self.monsters:
            if self.object_cards > 0:
                self.monsters[id]['level'] += 1
                self.object_cards -= 1
                return {'success': True, 'message': f"Monster {id} upgraded to level {self.monsters[id]['level']}"}
            else:
                return {'success': False, 'message': "No object cards left"}
        else:
            return {'success': False, 'message': "Monster does not exist"}


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
