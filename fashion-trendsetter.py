import re

def is_numeric(string):
    """Returns True if the string is numeric, False otherwise."""
    regex = re.compile(r'^\d+$')
    return regex.match(string) is not None

print("-->  Welcome to Fashion TrendSetter (:  <--")
print("A plateform that you can design your own outfit. including some tips to help your design more creative and unique.")
print("===><===")
first_name=input("Enter your first name : ")
last_name=input("Enter your last name : ")

gender = None
while True:
        print("1. Male, 2. Female")
        input_gender = input("Pick a gender : ")
        if input_gender == "1" or input_gender == "2":
            gender = int(input_gender)
            break
        else:
            print("Choose 1 or 2 ! Please try again.")
short_gender = ""
if(gender == 1): short_gender = "Mr."
if(gender == 2): short_gender = "Mrs."

phone_number=input("Enter your phone number : ")
email=input("Enter your email address : ")

while True:
    print("Do you want to see some tips before you start design ?")
    while True:
        yes_no = input("1. Yes, 2. No : ")
        if yes_no == "1" :
            print("Here is some tips : ")
            print("==>")
            print("1. Choose the right colors. Colors can make a big impact on your appearance. They can help you look more radiant, confident, and put-together. Choose colors that flatter your skin tone and hair color. You can also use color to create different moods and impressions. For example, bright colors can make you look more cheerful and approachable, while dark colors can make you look more sophisticated and mysterious.")
            print("==>")
            print("2. Mix and match patterns. Patterns can add interest and personality to your outfits. But be careful not to overdo it. Too many patterns can make you look busy and cluttered. A good rule of thumb is to stick to two patterns at most per outfit. You can mix and match different patterns, such as stripes and florals, or you can mix different sizes of the same pattern.")
            print("==>")
            print("3. Express yourself. Fashion is a great way to express your personality. Don't be afraid to experiment with different styles and trends.")
            break
        if yes_no == "2":
            break
        else:
            print("Please answer the question . :)")

    print("Ok let's go :)")

    # type 
    outfit_types = [
        'Wedding dress','Shorts','Jeans','Skirt',
        'T-shirt','Uniform','Swinsuit','Coat',
        'Suit','Dress','Trouser','Pants','Sports suit', 'Shoes'
    ]
    index = 1
    for outfit in outfit_types:
        print(str(index) + ". " + outfit)
        index += 1
    outfit_type_index = None
    while True:
        size_input = input("Please pick a type : ")
        if  is_numeric(size_input):
            total_index = len(outfit_types)
            if int(size_input) >= 1 and int(size_input) <= total_index :
                outfit_type_index = int(size_input) - 1
                break
        else:
            print("Please pick a valid type ):")

    # design for 
    users=['Man','Women','Girl','Boy']
    index = 1
    for user in users:
        print(str(index) + ". " + user)
        index += 1
    user_index = None
    while True:
        user_input = input("Who you design for ? : ")
        if  is_numeric(user_input):
            total_index = len(users)
            if int(user_input) >= 1 and int(user_input) <= total_index :
                user_index = int(user_input) - 1
                break
        else:
            print("Please pick a valid type of user ):")

    # size 
    sizes=['S','M','L','X','XL']
    index = 1
    for size in sizes:
        print(str(index) + ". " + size)
        index += 1
    size_index = None
    while True:
        size_input = input("Please pick a size : ")
        if  is_numeric(size_input):
            total_index = len(sizes)
            if int(size_input) >= 1 and int(size_input) <= total_index :
                size_index = int(size_input) - 1
                break
        else:
            print("Please pick a valid size ):")

    # color 
    colors=['red','blue','black','green','yellow', 'pink']
    index = 1
    for color in colors:
        print(str(index) + ". " + color)
        index += 1
    color_index = None
    while True:
        color_input = input("Please choose a color : ")
        if  is_numeric(color_input):
            total_index = len(colors)
            if int(color_input) >= 1 and int(color_input) <= total_index :
                color_index = int(color_input) - 1
                break
        else:
            print("Please pick a valid color ):")

    price = input("Alright Everything is seem to be done here. Please put a price on it. : $")
    price_kh = int(price) * 4000

    print("============================>")
    print(f"Congratulation { short_gender + ' ' + first_name + ' ' + last_name} you just design a product. here is your final design :)")

    print("Outfit => ", outfit_types[outfit_type_index])
    print("Design For => ", users[user_index])
    print("Size => ", sizes[size_index])
    print("Color => ", colors[color_index])
    print("Price USD => ", price)
    print("Price Riel => ", price_kh)
    print("============================>")

    restart = input("Write 'Yes' and press Enter if you want to restart. Press Enter to stop. Thank you : ")
    print("============================>")
    if restart == "Yes":
        pass
    else:
        break