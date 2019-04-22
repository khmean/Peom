"""
Program: poem.py
Author: Khann Mean
This program will define a poem class.
"""


class Poem(object):

    def __init__(self, author, title):
        """Constructor creates a Poem with author's name and title of the poem"""

        self.author = author
        self.title = title

    def getAuthor(self):
        """Returns the authors name"""
        return self.author

    def getTitle(self):
        """Returns the title"""
        return self.title

    def setContent(self, content):
        """Set the content of the poem"""
        self.content = content


    def getContent(self):
        """Return the content of the poem"""
        return self.content

    def __str__(self):
        return "Author: " + self.author + "\nTitle: " + self.title + "\n" + str(self.content) + "\n"


def main():

    p1 = Poem("John Doe", "Title")
    p1contentlist = []
    p1contentlist.append("This is the first line")
    p1contentlist.append("This is the second line")
    p1.setContent(p1contentlist)

    p2 = Poem("Jane Doe", "Title 2")
    p2contentlist = []
    p2contentlist.append("This is the first line")
    p2contentlist.append("This is the second line")
    p2.setContent(p2contentlist)

    p3 = Poem("Jay Doe", " Title 3")
    p3contentlist = []
    p3contentlist.append("This is the first line")
    p3contentlist.append("This is the second line")
    p3.setContent(p3contentlist)

    print(p1)
    print(p2)
    print(p3)


if __name__ == "__main__":
    main()
