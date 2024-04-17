print("Welcome to book store")
print("please login")
name=(input("Enter your name:"))
unm=int(input("Phone number:"))
add=input("Address:")
instock=["M.Math","E.English","F.French","P.Physics","H.history","B.Biology","C.Chemistry",
         "T.The Mortuary Collection","T1. The Devil's Candy","P1.Pontypool",
         "H1.Housebound","S.Southbound","T2.The Canal","G.Ghost Stories","S1.Summer of 84",
         "A.Afflicted","H2.Host","A1.A Dark Song","B.Brahma letter sets love","L.Logger 1",
         "L1.Logger 2","H3.Heart rate","T3.There is no tomorrow for us","W.Winter fire",
         "T4.Taste a young boy","I.It hides love","T5.That person is a dream",]
         
instock.sort()
print(instock)
book=input("Add to your cart:") 
many=int(input("How many?:"))
if book =="M":
    book=("Math")   
    print("\n")
    total=(5*many)
    print('',"book store\n","cash receipt\n","------------------------------------\n",
         " Order:",book,'5 x',many,"pc","Total:",total,'$\n',
         "Thank you for your order\n")
    
elif book =="E":
      book=("English")   
      print("\n")
      total=(10*many)
      print('',"book store\n","cash receipt\n","------------------------------------\n",
           " Order:",book,'10 x',many,"pc","Total:",total,'$\n',
           "Thank you for your order\n")
      
elif book =="F":
      book=("French")
      total=(10*many)
      print("\n")
      print('',"book store\n","cash receipt\n","--------------------------------------\n",
              "Order:",book,'10 x',many,"pc","\n","total:",total,'$\n',
              "Thank you for your order\n") 
      
elif book=="P":
    book=("physics")
    total=(5*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'5 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")
          
elif book=="H":
    book=("history")
    total=(5*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'5 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")
    
elif book =="B":
     book=("Biology")  
     total=(5*many)
     print("\n")
     print('',"book store\n","cash receipt\n","--------------------------------------\n",
           "Order:",book,'5 x',many,"pc","\n","total:",total,'$\n',
           "Thank you for your order\n")
     
elif book =="C":
     book=("Chemistry")  
     total=(5*many)
     print("\n")
     print('',"book store\n","cash receipt\n","--------------------------------------\n",
           "Order:",book,'5 x',many,"pc","\n","total:",total,'$\n',
           "Thank you for your order\n") 
     
elif book=="T":
    book=("The Mortuary Collection")
    total=(8*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")
          
elif book=="T1":
    book=("The Devil's Candy")
    total=(8*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")
          
elif book=="P1":
    book=("Pontypool")
    total=(10*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'10 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n") 

elif book=="H1":
    book=("Housebound")
    total=(8*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
    
elif book=="S":
    book=("Southbound")
    total=(7*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'7 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
    
elif book=="T2":
    book=("The Canal")
    total=(7*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'7 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             

elif book=="G":
    book=("Ghost Stories")
    total=(5.99*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'5.99 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
    
elif book=="S1":
    book=("Summer of 84")
    total=(8.04*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8.04 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")  
               
elif book=="A":
    book=("Afflicted")
    total=(8.11*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8.11 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
    
elif book=="H2":
    book=("Host")
    total=(9*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'9 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")  
               
elif book=="A1":
    book=("A Dark Song")
    total=(10.99*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'10.99 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")       
          
elif book=="B":
    book=("Brahma letter sets love")
    total=(8.99*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8.99 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")  
               
elif book=="L":
    book=("Logger 1")
    total=(7.50*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'7.50 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")   
              
elif book=="L1":
    book=("Logger 2")
    total=(7.50*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'7.50 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")          
       
elif book=="H3":
    book=("Heart rate")
    total=(8*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'8 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
 
elif book=="T3":
    book=("There is no tomorrow for us")
    total=(10*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'10 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
   
elif book=="W":
    book=("Winter fire")
    total=(9*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'9 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             
    
elif book=="T4":
    book=("Taste a young boy")
    total=(7*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'7 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")             

elif book=="I":
    book=("It hides love")
    total=(10*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'10 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")     
            
elif book=="T5":
    book=("That person is a dream")
    total=(9.99*many)
    print("\n")
    print('',"book store\n","cash receipt\n","--------------------------------------\n",
          "Order:",book,'9.99 x',many,"pc","\n","total:",total,'$\n',
          "Thank you for your order\n")    


class studyApp:
    def __init__(self):
        self.flashcards = {}
        self.quizzes = {}

    def add_flashcards(self,topic,question,answer):
        if topic in self.flashcards:
            self.flashcards[topic].append((question,answer))
        else:
            self.flashcards[topic] = [(question,answer)]

    def add_quiz(self,topic,questions,answers):
        if topic in self.quizzes:
            self.quizzes[topic].append((questions,answers)) 
        else:
            self.quizzes[topic] = [(questions,answers)]
    def study_flashcards(self,topic):
        if topic in self.flashcards:
            for card in self.flashcards[topic]:
                print(f"Question.{[1]}")
                input("Press enter to see the answer:")
                print(f"Answer:{card[1]}")

        else:
            print("No flashcards available for this topic")

    def take_quiz(self,topic):
        if topic in self.quizzes:
            score = 0
            for quiz in self.quizzes[topic]:
                questions, answers = quiz
                for i, question in enumerate(questions):
                    user_answer = input(f"{i+1} {question}")
                    if user_answer == answers[i]:
                        score += 1
                print(f"You scored {score} out of {len(questions)}")
        else:
            print("No quizzes available for this topic")

#Example usage
app = studyApp()
app.add_flashcards("Math","What is 2023+2024?","4047")
app.add_flashcards("Math","what is the square root of 16?","4")
app.add_flashcards("Science","What is the powerhouse of the call?","Mitochondria")

app.add_quiz("Math",["What is 5*5?","What is 10/2?"],["25","5"])
app.add_quiz("Science",["What ais the chemicsl symbol for wather?",
            "What is the Earth's largest continent?"],["H2O","Asian"])
app.study_flashcards("Math")
app.take_quiz("Math")
class Document :
    def __init__(self,title,author,content) :
        self.title = title
        self.author = author
        self.content = content

class Documentstore:
    def __init__(self):
        self.document =[]
    def add_document(self, document):
        self.document.append(document)
    
    def find_document(self, title):
        for document in self.document:
            if title.lower() in document.title.lower():
                return document
         

        return None
        
    def lisf_document(self):
        if not self.document:
            print("the document store is empty.")
        else:
            print("list of Documents: ")
            for document in self.document:
                print(f"Title: {document.title},Author: {document.author}< content: {document.content}")

class Book:
    def __init__(self,title, author,price):
        self.title = title
        self.author = author
        self.price = price

class Bookstore:
    def __init__(self):
        self.book=[]

    def add_book(self, book):
        self.book.append(book)

    def find_book(self, title):
        for book in self.book:
            if title.lower() in book.title.lower():
                return book
         

        return None
        
    def list_book(self):
        if not self.book:
            print("The book store is empty.")
        else:
            print("list of Books: ")
            for book in self.books:
                print(f"title: {book.title}, Author: {book.author}, price: ${book.price}")

document_store = Documentstore()
bookstore = Bookstore()

document_store.add_document(Document("document 1","lin Mongkolsery","cal1-ch1 TD 1"))
document_store.add_document(Document("document 2"," lin Mongkolsery " ,"cal1-ch2 TD 2"))
document_store.add_document(Document("document 3"," lin Mongkolsery ","cal2-ch3 TD 3"))
document_store.add_document(Document("document 4","longsovann","2e principe TD 1"))
document_store.add_document(Document("document 5","longsovann","1e principe TD 11"))
document_store.add_document(Document("document 6","longsovann","2e principe TD 10"))
document_store.add_document(Document("document 7","BUNRA ","TD 1"))
document_store.add_document(Document("document 8","BUNRA " ,"Travaill 18 Ex1"))
document_store.add_document(Document("document 9","longsovann", "statique des Fluides "))
document_store.add_document(Document("document 10","chetha ","Enerige Ex 4"))
document_store.add_document(Document("document 11","chan sophal","Main_code"))
document_store.add_document(Document("document 12","pukbunna","cal1-ch6.TD 6"))
document_store.add_document(Document("document 13","pukbunna","cal2-ch4 power series"))
document_store.add_document(Document("document 14","lin Mongkolsery","TD 1"))
document_store.add_document(Document("document 15","CHETHA","TD 6"))
document_store.add_document(Document("document 16","BUNRA 1","TD 2"))


bookstore.add_book(Book("Bold","Emily bronte",12.99))
bookstore.add_book(Book("5 Minute calm","J.R.R.tolkien",9.00))
bookstore.add_book(Book("7 Habits ","Anna riche",10.00))
bookstore.add_book(Book("All in","Dan brown",7.00))
bookstore.add_book(Book("Be your best boss","Ruskin bond",9.99))
bookstore.add_book(Book("Alibaba","Lord byron",12.00))
bookstore.add_book(Book("Be excellent at anything ","Anthony",10.50))
bookstore.add_book(Book("How to lead others","Alexandre",12.50))
bookstore.add_book(Book("The google story","George saunders",12.00))
bookstore.add_book(Book("21 year","Charlotte",12.20))
bookstore.add_book(Book("7 secerts","Alisa xino",16.99))
bookstore.add_book(Book("Business","L.K Rowling",12.99))
bookstore.add_book(Book("Self help","Stephen King",14.99))
bookstore.add_book(Book("Econoic","Oscar wilde",15.00))
bookstore.add_book(Book("18 minutes find you","Loisa",12.59))
bookstore.add_book(Book("Victory !","Jane",13.00))
bookstore.add_book(Book("14000 things to be happy about","Jokkey",9.00))

while True:
    print("\nwelcome to the book and document store project in python.")
    print("1. search for a document")
    print("3. list all Documents")
    print("4.list all books")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the document title you're looking for: ")
        document = document_store.find_document(title)
        if document:
            print(f"Title: {document.title}\nAuthor: {document.author}\nContent: {document.content}")
        else:
            print(f"No document with the title '{title}' found.")

    elif choice == "2":
        title = input("Enter the book title you're looking for: ")
        book = bookstore.find_book(title)
        if book:
            print(f"Title: {book.title}\nAuthor: {book.author}\nPrice: ${book.price}")
        else:
            print(f"No book with the title '{title}' found.")

    elif choice == "3":
        document_store.list_documents()

    elif choice == "4":
        bookstore.list_books()

    elif choice == "5":
        print("Thank you for purchasing books and documents from my store. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")