from collections import deque

# Graph data
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def breadth_first_search(name):
    search_queue = deque()  # Creates a new queue
    search_queue += graph[name]  # Adds all of your neighbors to the search queue
    searched = []  # This array is how you keep track which people you've searched before

    while search_queue:  # While the queue isn't empty ...
        person = search_queue.popleft()  # ... grabs the first person off the queue
        if not person in searched:  # Only search this person if you haven't already searched them.
            if person_is_seller(person):  # Checks whether the person is a mango seller
                print("%s is a mango seller!" % person)  # Yes, they're a mango seller.
                return True
            else:
                search_queue += graph[person]  # No, they aren't. Add all of this person's friends to the search queue
                searched.append(person)  # Marks this person as searched
    return False  # If you reached here, no one in the queue was a mango seller.


def person_is_seller(name):
    """This function checks whether the person's name ends with the letter m.
    If it does, they're a mango seller."""
    return name[-1] == 'm'


if __name__ == "__main__":
    if not breadth_first_search("you"):
        print("Mango seller not found")
