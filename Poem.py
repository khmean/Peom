"""
Program: poem.py
Author: Khann Mean
This program will define a poem class.
"""


class Poem(object):

    def __init__(self, author, title):
        """Contructor creates a Poem with author's name and title of the poem"""

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
        #self.content.append(0)


    def getContent(self):
        """Return the content of the poem"""
        return self.content

    def __str__(self):
        return "Author: " + self.author + "\nTitle: " + self.title + "\n" + str(self.content)


def main():
    p = Poem("John Doe", "Title")

    p.setContent("This is the first line")



    print(p)


if __name__ == "__main__":
    main()
