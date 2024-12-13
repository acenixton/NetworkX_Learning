
class Person():
    
    def __init__(self, name):
        self.name = name
        self.relationships = {}
        
    def __str__(self):
        names = []
        relations = []
        ausgabe = f"\n{self.name}'s relationships:\n"
        width = max([len(pers.name) for pers in self.relationships.keys()])
        for pers, rel in self.relationships.items():
            ausgabe += f"{pers.name:<{width}}: {rel}\n"
            names.append(pers.name)
            relations.append(rel)
        
        return ausgabe

    def set_relation(self, other, type):
        valid_types = ['sibling', 'friend', 'partner', 'aquaintance', 'collegue', 'grandparent', 'grandchild', 'parent',  'child']
        dir_types = valid_types[5::]
        if type in valid_types:
            self.relationships.update({other:type})
            # also sets appropriate relation for other Person
            if type in dir_types:
                match type:
                    case 'grandparent':
                        other.relationships.update({self:'grandchild'})
                    case 'parent':
                        other.relationships.update({self:'child'})
                    case 'grandchild':
                        other.relationships.update({self:'grandparent'})
                    case 'child':
                        other.relationships.update({self:'parent'})
            else:
                other.relationships.update({self:type})
        else:
            raise ValueError("Relationship is not of valid type!")
        
    
    def get_relations(self):
        return self.retalionships
    

# tine = Person('Tine')
# marlon = Person('Marlon')
# lydi = Person('Lydi')
# dieter = Person('Dieter')
# tine.set_relation(marlon, 'sibling')
# tine.set_relation(lydi, 'sibling')
# tine.set_relation(marlon, 'sibling')
# tine.set_relation(dieter, 'grandparent')
# print(tine)
# print(dieter)
    