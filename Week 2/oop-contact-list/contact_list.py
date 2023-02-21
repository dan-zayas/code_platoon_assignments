class ContactList:
    #Initialization
    def __init__(self, category, contacts):
        self.category = category
        self.contacts = contacts

    def add_contact(self, info):
        #should add a new contact to the list, while keeping the list sorted
        self.contacts.append(info)
        #sort the contacts anytime a person is added.
        self.contacts = sorted(self.contacts, key=lambda d: d['name'])
        return self.contacts

    def remove_contact(self, name):
        #should remove a contact from the list by name.
        for index in range(len(self.contacts)-1):
            if self.contacts[index]['name'] == name:
                self.contacts.remove(self.contacts[index])
        return self.contacts

    def find_shared_contacts(self, contact_list):
        #should accept another contact list as an argument, and then return a new ContactList to indicate all the contacts that appear in both lists (exact same name and phone number).
        return [x for x in contact_list.contacts if x in self.contacts]

#Declarations and Instantiation
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'},{'name':'Carlos', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

add_friend = my_friends_list.add_contact({'name':'April','number':'555-5555'})
print(add_friend)

remove_april = my_friends_list.remove_contact('April')
print(remove_april)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)