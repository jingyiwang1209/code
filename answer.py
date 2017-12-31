class Node():
    def __init__(self, value):
        self.val = value
        self.next = None


class generateSizeOfFriends():
    # for verifying if two words have one Levenshtein distance or not.
    def isOneLevenshtein_distance(self, s, t):
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False

        if m > n:
            return self.isOneLevenshtein_distance(t, s)

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                return s[i:] == t[i + 1:]

        # the string is its own social network, if the two strings are the same, the size will still be 1.
        return True

    # for processing  the linked list:
    # if two words have one Levenshtein distance, remove the word in the linked list (O(1)) to avoid infinite loop
    # otherwise, keep looping until finds the target word
    def processLinkedList(self, len_q, map, q, temp):
        potential_network_head = map[len_q]
        dummy = Node(0)
        dummy.next = potential_network_head
        prev = dummy

        while potential_network_head:
           if self.isOneLevenshtein_distance(q, potential_network_head.val):
               temp.append(potential_network_head.val)
               prev.next = potential_network_head.next
               potential_network_head = prev

           prev = potential_network_head
           potential_network_head = potential_network_head.next

        map[len_q]= dummy.next


    def social_network_size(self, dic, keyword):
        if keyword is None or len(keyword)== 0 or dic is None or len(dic) == 0:
            return 0

        result=[]
        queue=[keyword]

        # use a dictionary to store the data as key-value pairs:
        # { lengthOfWordsInTheSameLength: Node(word1)->Node(word2)->Node(word3)... }
        # So a length is a key, and a linked list of the words with the same length is a value
        map = {}
        # append node in the linked list. O(1) since append the node before the head every time
        for word in dic:
            node = Node(word)
            length = len(word)
            if length in map:
                cur = map[len(word)]
                node.next = cur
            map[len(word)] = node

        while queue:
            result+=queue
            temp = []
            for q in queue:
                # each word has 3 potential friend network:
                # the one with the same length, the one with length-1 and the one with length+1
                len1 = len(q)
                len2  = len(q)-1
                len3  = len(q)+1

                if len1 in map:
                    self.processLinkedList(len1, map, q, temp)
                if len2 in map:
                    self.processLinkedList(len2, map, q, temp)

                if len3 in map:
                    self.processLinkedList(len3, map, q, temp)

            queue = temp

        return len(result)-1



generateSizeOfFriends = generateSizeOfFriends()
# test case1
dic1 = ['HI','HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
keyword1='HI'
print(generateSizeOfFriends.social_network_size(dic1, keyword1))
# # output: 7
# (['HI', 'HE', 'HER', 'SHE', 'HERE', 'HEAR', 'THERE'])


# test case2
dic2=[]
dictionary2 = open('very_small_test_dictionary.txt', 'r').read()
lst2 = dictionary2.split('\n')
for line in lst2:
  if(len(line) > 0):
    dic2.append(line)
keyword2= 'LISTY'
print(generateSizeOfFriends.social_network_size(dic2, keyword2))
# output:5
# ['LISTY', 'LISTS', 'LUSTY', 'FISTS', 'FIST']


# test case 3
dic3=[]
dictionary3 = open('dictionary.txt', 'r').read()
lst3 = dictionary3.split('\n')
for line in lst3:
    if(len(line) > 0):
        dic3.append(line)
keyword3= 'LISTY'
print(generateSizeOfFriends.social_network_size(dic3, keyword3))
# output:51710