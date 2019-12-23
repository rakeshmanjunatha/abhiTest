# class BookStore:
#     noOfBooks = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         BookStore.noOfBooks += 1
#
#     def bookInfo(self):
#         print("Book title:", self.title)
#         print("Book author:", self.author, "\n")
#
#
# # Create a virtual book store
# b1 = BookStore("Great Expectations", "Charles Dickens")
# b2 = BookStore("War and Peace", "Leo Tolstoy")
# b3 = BookStore("Middlemarch", "George Eliot")
#
# # call member functions for each object
# b1.bookInfo()
# b2.bookInfo()
# b3.bookInfo()
#
# print("BookStore.noOfBooks:", BookStore.noOfBooks)
#
#
# # Parent class 1
# class TeamMember(object):
#     def __init__(self, name, uid):
#         self.name = name
#         self.uid = uid
#
#     # Parent class 2
#
#
# class Worker(object):
#     def __init__(self, pay, jobtitle):
#         self.pay = pay
#         self.jobtitle = jobtitle
#
#     # Deriving a child class from the two parent classes
#
#
# class TeamLeader(TeamMember, Worker):
#     def __init__(self, name, uid, pay, jobtitle, exp):
#         self.exp = exp
#         TeamMember.__init__(self, name, uid)
#         Worker.__init__(self, pay, jobtitle)
#         print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp))
#
#
# TL = TeamLeader('Jake', 10001, 250000, 'Scrum Master', 5)


# class A:
#     def __init__(self, i = 0):
#         self.i = i
#
#
# class B(A):
#     def __init__(self, j = 0):
#         self.j = j
#         # A.__init__(self, 2)
#
#
# def main():
#     b = B()
#     print(b.i)
#     print(b.j)
#
# main()


# class A:
#     def __init__(self):
#         self.calcI(30)
#         print("i from A is", self.i)
#
#     def calcI(self, i):
#         self.i = 2 * i;
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#
#     def calcI(self, i):
#         self.i = 3 * i;
#
#
# b = B()

# print  (u'2.15'.isnumeric())
# identity = ['Python', 'Python quiz', 'Python String', 'Python Interview', 'Python questions']
# print ("\n".join(identity))
# print  ('+55'.zfill(5))
# str='abababadaadbbaccabc'
# print  (str.count('ab',-17,-1))
#
# str='PYTHON\nString\nConcepts'
# print  (str.splitlines())
#
# str='abcdefcdyz'
# print  (str.partition('cd'))
#
# str='python'
# print  (str.center(15,'*'))
#
# str='Hello@John!!'
# print  (str.lower())
#
# str='example'
# print  (str.center(8,'#'))

# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# # list2 = extendList(123,[])
# list3 = extendList('a')
#
# print("list1 = %s" % list1)
# # print("list2 = %s" % list2)
# # print("list3 = %s" % list3)
#
#
# list = ['a', 'b', 'c', 'd', 'e']
# print (list[10:])




# from datetime import datetime
#
#
# class Comment(object):
#     def __init__(self, email, content, created=None):
#         self.email = email,
#         self.content = content
#         self.created = created or datetime.now()
#
#
# comment = Comment('rakesh@gmail.com', 'foo bar')
#
#
# from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
#
# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()
#
#
# ser = CommentSerializer(comment)
# print(ser.data['email'])
#
# json = JSONRenderer().render(ser.data)
# print(json)

import requests
import json
#  GET
resp = requests.get('http://api.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id,abstract&wt=json&indent=on')
print(resp.json()['response']['numFound'])

# POST
input_data = {}
resp = requests.post('url', json=input_data)
if resp.status_code != 201:
    print('error')
# print(resp.json()['id'])

resp = requests.post('url', data=json.dumps(input_data), headers={'Content-Type': 'application/json'})



