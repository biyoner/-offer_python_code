#coding= utf-8
#author:Biyoner
import collections
class CharStatistics(object):
    def __init__(self):
        self.occurrrence = collections.OrderedDict()

    def Insert(self,ch):

        if self.occurrrence.has_key(ch):
            if self.occurrrence[ch] >0:
                self.occurrrence[ch] = -2
        else:
            self.occurrrence[ch] = 1


    def FirstAppearingOnce(self):
        val = ""
        for key in self.occurrrence.keys():
            if self.occurrrence[key] >0:
                val = key
                break
        return val

def Test(name, ch,expectedValue):
    if ch.FirstAppearingOnce() == expectedValue:
        print name + " is passed !"
    else:
        print name + " is failed !"


if __name__ == "__main__":
    chars = CharStatistics()

    Test("Test1", chars, "")

    chars.Insert("g")
    Test("Test2", chars, 'g')

    chars.Insert('o')
    Test("Test3", chars, 'g')

    chars.Insert('o')
    Test("Test4", chars, 'g')

    chars.Insert('g')
    Test("Test5", chars, "")

    chars.Insert('l')
    Test("Test6", chars, 'l')

    chars.Insert('e')
    Test("Test7", chars, 'l')
