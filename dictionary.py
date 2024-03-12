# dictionary = {
#     "leisure" : "casual",
#     "subdue" : "to bring a territory or people under control by force",
#     "by means of " : "with the help of; by using",
#     "bankrupe" : "(of a person or organization) declared in law as unable to pay their debts",
#     "clipboard" : "a temporary storage area where a copied or cut material is kept for pasting into another place",
#     "cache" : "an auxiliary memory from which high-speed retrieval is possible",
#     "acknowledge" : "admit the truth of",
#     "audit" : "an official inspection of an organization's account, typically by an independent body"
# }
# search = input("Search for a word : ").lower()
# print(f"{search} : {dictionary.get(search,'Value not found!')}") # the get method is used to supply the value,
# .get(key, "message") if the key is not present then a message will be returned

# print(f"{search} : {dictionary[search]}")
#################################################################################################################
# emojiD = {
#     ":)" : "😊",
#     ":(" : "🙁",
#     ":|" : "😐"
# }
# message = input("Enter a message : ")
# splittedM = message.split()
# output = ""
# for word in splittedM:
#     output = output + emojiD.get(word, word) + " "
# print(output)
#################################################################################################################
# dictionary = {
#     'asap' : 'As Soon As Possible',
#     'wtf' : 'What The ***',
#     'ty' : 'Thank You',
#     'idk' : "I Don't Know",
#     'btw' : 'By The way'
# }
# text = input("Enter text: ")
# splittedText = text.split()
# translated_text = ""
# for word in splittedText:
#     translated_text = translated_text + dictionary.get(word,word) + ' '
# print("Original Text is following:")
# print(translated_text)
#################################################################################################################
# def dictionary(text):
#     splittedText = text.split()
#     translatedText = ""
#     dict = {
#         1 : "one",
#         2 : 'two',
#         3 : 'three',
#         'idk' : "I don't know",
#         'ty' : "Thank You",
#         'btw' : 'By the way',
#         ':)' : '😊',
#         ':(' : '☹',
#         ':|' : '😐'
#     }
#     for word in splittedText:
#         translatedText = translatedText + dict.get(word,word) + " "
#     return translatedText
#
# enter_text = input("Enter text:")
# print(f"{dictionary(enter_text)}")
#################################################################################################################
def process(key):
    dictionary = {
        'hi' : 'High',
        'lo' : 'Low',
        'ty' : 'Thank You',
        'btw': 'By The Way',
        'asap' : 'As Soon As Possible'
    }
    return dictionary.get(key.lower(),"There's no as such word in dictionary")

print(f"Full form of btw is {process('bTW')}")

