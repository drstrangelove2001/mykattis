import sys

class Person:
    def __init__(self, name):
        self.name = name
        self.behind = None
        self.front = None
        self.partner = None

class Congaline:
    def __init__(self, length):
        self.first = None
        self.length = length

    def pushPersonToBack(self, person):
        if self.first is None:
            self.first = person
            self.first.behind = self.first
            self.first.front = self.first
        else:
            last_person = self.first.front
            person.behind = self.first
            person.front = last_person
            last_person.behind = person
            self.first.front = person

    def removePerson(self, curr):
        if self.first is None:
            return
        if curr == self.first:
            if curr.behind == self.first:
                self.first = None
            else:
                self.first = curr.behind
            if curr.front != curr:
                curr.front.behind = self.first
            self.first.front = curr.front
        else:
            curr.front.behind = curr.behind
            curr.behind.front = curr.front
        return

    def insertBehindPartner(self, person):
        if self.first is None:
            return
        ptr = person.partner
        person.behind = ptr.behind
        person.front = ptr
        ptr.behind = person
        person.behind.front = person

    def showCongaline(self):
        curr = self.first
        for _ in range(self.length):
            print(curr.name)
            curr = curr.behind

N,Q = map(int, input().split())
line = Congaline(2*N)
for _ in range(N):
    c1,c2 = [Person(x) for x in sys.stdin.readline().split()]
    c1.partner, c2.partner = c2,c1
    line.pushPersonToBack(c1)
    line.pushPersonToBack(c2)

mic = line.first
for move in sys.stdin.readline():
    if move == 'P':
        print(mic.partner.name)
    elif move == 'F':
        mic = mic.front
    elif move == 'B':
        mic = mic.behind
    elif move == 'R':
        tmp = mic.behind
        line.removePerson(mic)
        line.pushPersonToBack(mic)
        mic = tmp
    elif move == 'C':
        tmp = mic.behind
        line.removePerson(mic)
        line.insertBehindPartner(mic)
        mic = tmp

print()
line.showCongaline()