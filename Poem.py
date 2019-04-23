"""
Program: poem.py
Author: Khann Mean
This program will define a poem class.
"""


class Poem(object):
    # Initialize the number of poems to 0
    num_of_poems = 0

    def __init__(self, author, title):
        """Constructor creates a Poem with author's name and title of the poem"""
        self.author = author
        self.title = title
        # Increment the amount of Poems used
        Poem.num_of_poems += 1

    def getAuthor(self):
        """Returns the authors name"""
        return self.author

    def getTitle(self):
        """Returns the title"""
        return self.title

    def setContent(self, content):
        """Set the content of the poem"""
        self.content = content

    def setHaiku(self):
        """Test to see if the poem is a Haiku and return false if not a Haiku"""
        Haiku = False
        return Haiku

    def __str__(self):
        return "Author: " + self.author + "\nTitle: " + self.title


def main():
    # Assign the first poem to class Poem
    p1 = Poem("Alfred Lord Tennyson", "The Eagle")
    p1contentlist = []
    p1contentlist.append("He clasps the crag with crooked hands;")
    p1contentlist.append("Close to the sun in lonely lands,")
    p1contentlist.append("Ring’d with the azure world, he stands.")
    p1contentlist.append("The wrinkled sea beneath him crawls;")
    p1contentlist.append("He watches from his mountain walls,")
    p1contentlist.append("And like a thunderbolt he falls.")
    p1.setContent(p1contentlist)

    # Assign the second poem to class Poem
    p2 = Poem("Gelett Burgess", "Purple Cow")
    p2contentlist = []
    p2contentlist.append("I never saw a Purple Cow,")
    p2contentlist.append("I never hope to see one,")
    p2contentlist.append("But I can tell you, anyhow,")
    p2contentlist.append("I'd rather see than be one!")
    p2.setContent(p2contentlist)

    # Assign the third poem to class Poem
    p3 = Poem("Robert Frost", "Fire and Ice")
    p3contentlist = []
    p3contentlist.append("Some say the world will end in fire,")
    p3contentlist.append("Some say in ice.")
    p3contentlist.append("From what I've tasted of desire")
    p3contentlist.append("I hold with those who favor fire.")
    p3contentlist.append("But if it had to perish twice,")
    p3contentlist.append("I think I know enough of hate")
    p3contentlist.append("To say that for destruction ice")
    p3contentlist.append("Is also great")
    p3contentlist.append("and would suffice.")
    p3.setContent(p3contentlist)

    # print the results of the Poem class
    print(p1)
    print("Is poem: {} a Haiku? ".format(p1.getTitle()))
    print(p1.setHaiku())
    print("")
    for p1index in range(len(p1.content)):
        print(p1.content[p1index])

    print("")
    print(p2)
    print("Is poem: {} a Haiku? ".format(p2.getTitle()))
    print(p2.setHaiku())
    print("")
    for p2index in range(len(p2.content)):
        print(p2.content[p2index])

    print("")
    print(p3)
    print("Is poem: {} a Haiku? ".format(p3.getTitle()))
    print(p3.setHaiku())
    print("")
    for p3index in range(len(p3.content)):
        print(p3.content[p3index])
    print("")
    # Print the number of Poem instances that were used
    print("There was {}".format(Poem.num_of_poems) + " poems.")


if __name__ == "__main__":
    main()
