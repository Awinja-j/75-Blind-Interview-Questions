class Trie:

    def __init__(self):
        self.root = dict()
        self._end = '*'

    ## takes in a list of words
    def make_trie(self, *words):
        ## creates our root dict()
        trie = dict()

        for word in words:
            ## create a temporary dict based off our root
            ## dict object
            temp_dict = trie

            for letter in word:
                ## update our temporary dict and add our current
                ## letter and a sub-dictionary
                temp_dict = temp_dict.setdefault(letter, {})

            ## If our word is finished, add {'*': '*'}
            ## this tells us our word is finished
            temp_dict[self._end] = self._end
        return trie




    def find_word(self, trie, word):
        sub_trie = trie
        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        else:
            if self._end in sub_trie:
                return True
            else:
                return False



    def add_word(self,trie, word):
        ## We want to catch if a word already
        ## exists within our trie structure
        if self.find_word(trie, word):
            print("Word Already Exists")
            ## if it does just return our original trie
            return trie

        ## if it doesn't we want to add the new word
        temp_trie = trie
        for letter in word:
            ## iterate through our word and see how
            ## much of the word we already have within our
            ## structure
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                temp_trie = temp_trie.setdefault(letter, {})

        ## Terminate our new word
        temp_trie[self._end] = self._end
        ## return our new trie object
        return temp_trie
T = Trie()
trie = T.make_trie('hi', 'hello', 'howdy')

print(trie)

res = T.find_word(trie, 'hi')

print(res)

add = T.add_word(trie, 'high')

print(add)

res2 = T.find_word(trie, 'high')

print(res2)