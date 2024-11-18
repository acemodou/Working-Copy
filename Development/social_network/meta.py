from collections import deque
from typing import List, Dict, Optional

class Person:
    def __init__(self, person_id: int):
        self.person_id = person_id
        self.info = ""
        self.friends = []

    def get_info(self) -> str:
        return self.info

    def set_info(self, info: str):
        self.info = info

    def get_friends(self) -> List[int]:
        return self.friends

    def get_id(self) -> int:
        return self.person_id

    def add_friend(self, friend_id: int):
        self.friends.append(friend_id)


class PathNode:
    def __init__(self, person: Person, previous_node: Optional['PathNode'] = None):
        self.person = person
        self.previous_node = previous_node

    def get_person(self) -> Person:
        return self.person

    def collapse(self, starts_with_root: bool) -> List[Person]:
        path = []
        node = self
        while node is not None:
            if starts_with_root:
                path.append(node.person)
            else:
                path.insert(0, node.person)
            node = node.previous_node
        return path


class BFSData:
    def __init__(self, root: Person):
        self.to_visit = deque([PathNode(root)])
        self.visited = {root.get_id(): PathNode(root)}

    def is_finished(self) -> bool:
        return len(self.to_visit) == 0


def merge_paths(bfs1: BFSData, bfs2: BFSData, connection: int) -> List[Person]:
    end1 = bfs1.visited[connection]
    end2 = bfs2.visited[connection]

    path1 = end1.collapse(False)  # end -> source
    path2 = end2.collapse(True)   # source -> end

    path2.pop(0)  # remove connection node in path2
    path1.extend(path2)  # add second path
    return path1


def search_level(people: Dict[int, Person], primary: BFSData, secondary: BFSData) -> Optional[Person]:
    count = len(primary.to_visit)
    for _ in range(count):
        path_node = primary.to_visit.popleft()
        person_id = path_node.get_person().get_id()

        if person_id in secondary.visited:
            return path_node.get_person()

        person = path_node.get_person()
        for friend_id in person.get_friends():
            if friend_id not in primary.visited:
                friend = people[friend_id]
                next_node = PathNode(friend, path_node)
                primary.visited[friend_id] = next_node
                primary.to_visit.append(next_node)
    return None


def find_path_bi_bfs(people: Dict[int, Person], source_id: int, dest_id: int) -> Optional[List[Person]]:
    source = people[source_id]
    dest = people[dest_id]
    
    source_data = BFSData(source)
    dest_data = BFSData(dest)

    while not source_data.is_finished() and not dest_data.is_finished():
        # Search out from source
        collision = search_level(people, source_data, dest_data)
        if collision is not None:
            return merge_paths(source_data, dest_data, collision.get_id())

        # Search out from destination
        collision = search_level(people, dest_data, source_data)
        if collision is not None:
            return merge_paths(source_data, dest_data, collision.get_id())

    return None


class Machine:
    def __init__(self, machineID):
        self.machineID = machineID
        self.personToMachineID = {}
        self.machineIDToPersonID = {}

    def getPersonWithID(self, personID):
        return self.machineIDToPersonID.get(personID)

    def getMachineWithID(self, machineID):
        return self.personToMachineID.get(machineID)


class Server:
    def __init__(self):
        self.machines = {}
        self.personToMachineID = {}
        self.machineIDToPersonID = {}

    def getMachineIDForUser(self, personID):
        return self.personToMachineID.get(personID)

    def getPersonWithID(self, personID):
        machineID = self.getMachineIDForUser(personID)
        if machineID is None:
            return None
        machine = self.getMachineWithID(machineID)
        if machine is None:
            return None
        return machine.getPersonWithID(personID)

    def getMachineWithID(self, machineID):
        return self.machines.get(machineID)


# Example usage
server = Server()
machine1 = Machine(1)
machine2 = Machine(2)

server.machines[1] = machine1
server.machines[2] = machine2

server.personToMachineID[101] = 1
server.personToMachineID[102] = 2

machine1.machineIDToPersonID[101] = "Person 101"
machine2.machineIDToPersonID[102] = "Person 102"

print(server.getPersonWithID(101))  # Output: Person 101
print(server.getPersonWithID(102))  # Output: Person 102

# Example usage of the bi-directional BFS
people = {
    1: Person(1),
    2: Person(2),
    3: Person(3),
    4: Person(4)
}

people[1].add_friend(2)
people[2].add_friend(1)
people[2].add_friend(3)
people[3].add_friend(2)
people[3].add_friend(4)
people[4].add_friend(3)

path = find_path_bi_bfs(people, 1, 3)
if path:
    print("Path found:")
    for person in path:
        print(person.get_id())
else:
    print("No path found")