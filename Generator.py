

import requests


url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"number":"1","limitLicense":"false"}
vegetarian_querystring = {"tags":"vegetarian","number":"1","limitLicense":"true"}
vegan_querystring = {"tags":"vegan","number":"1","limitLicense":"true"}
#API Key needed
headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": ""
}

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

# user input first question
while True:


    program= input("Welcome! Do you want to receive a random recipe? Please select 'Yes' or 'q' to quit: ").lower()
    if program=="yes":
        print("Awesome! Let's keep going")
        break

    elif program=="q":
           print("Okay, Thanks for using the program!")
           break
    else:
           print("Invalid option -- Please check spelling and try again")



#user input second question


while True:           
    if program=="yes":
        dietchooser= (input(" Please enter 'randomized' to continue or 'specific diet' for a certain dietary restriction :").lower())

    if program == "yes" and dietchooser == "randomized":
        print("Perfect!,here comes your random recipe!")
        break

    elif program == "yes" and dietchooser == "specific diet":
        print("No problem!, see options below:")
        print("\n")
        break

    elif program == "q":
        break

    else:
        print("Invalid option -- please enter either 'specific diet' or 'randomized':")


choices=['Vegetarian', 'Vegan']  




#user input second question
while True:
    if program== "yes" and dietchooser=="specific diet":
        print(*choices, sep = ", ")
        userdecision= input("Please select 'Vegetarian' or 'Vegan':").lower()
    elif program=="q":
        break

    elif dietchooser=="randomized":
        break    

    if userdecision == "vegetarian":
        print(f" No problem! Here comes your random {userdecision} recipe")
        break

    elif userdecision == "vegan":
        print(f" No problem! Here comes your random {userdecision} recipe")
        break




    else:
        print("Invalid option -- please try again")




     #setting results for each possible choice by user

randomresults=requests.get(url, headers=headers, params=querystring)

vegetarianresults=requests.get(url, headers=headers, params=vegetarian_querystring)  

veganresults=requests.get(url, headers=headers, params=vegan_querystring)


# setting cleaning up each result from user choice     
myJSON=randomresults.json()

myJSON2=vegetarianresults.json()

myJSON3=veganresults.json()




recipes=myJSON['recipes'][0]

vegetarianrecipes=myJSON2['recipes'][0]

veganrecipes=myJSON3['recipes'][0]



#basic random recipe variables
name = recipes['title']
instructions= recipes['instructions']
mealprice=recipes['pricePerServing']
summary=recipes['summary']
servings= recipes['servings']
dishtype= recipes['dishTypes'][0]
vegetarian= recipes['vegetarian']
vegan= recipes['vegan']
glutenfree=recipes['glutenFree']
dairyfree=recipes['dairyFree']

#vegetarian recipe variables
vegetarian_name = vegetarianrecipes['title']
vegetarian_instructions= vegetarianrecipes['instructions']
vegetarian_mealprice=vegetarianrecipes['pricePerServing']
vegetarian_summary=vegetarianrecipes['summary']
vegetarian_servings= vegetarianrecipes['servings']
vegetarian_dishtype= vegetarianrecipes['dishTypes'][0]
veg_vegetarian= vegetarianrecipes['vegetarian']
vegetarian_vegan= vegetarianrecipes['vegan']
vegetarian_glutenfree=vegetarianrecipes['glutenFree']
vegetarian_dairyfree=vegetarianrecipes['dairyFree']
#vegan recipe variables
vname = veganrecipes['title']
vinstructions= veganrecipes['instructions']
vmealprice= veganrecipes['pricePerServing']
vsummary= veganrecipes['summary']
vservings= veganrecipes['servings']
vdishtype= veganrecipes['dishTypes'][0]
vvegetarian= veganrecipes['vegetarian']
vvegan= veganrecipes['vegan']
vglutenfree=veganrecipes['glutenFree']
vdairyfree=veganrecipes['dairyFree']


def getrandomrecipe(program):
    if program == "yes" and dietchooser == "randomized":
     print(name)
     print(instructions)
     #print(Ingredients)
     print(mealprice)
     #print(preptime)
     #print(cooktime)
     #print(summary)
     print(dishtype)
     print(servings)
     return (name, instructions, mealprice, servings,  dishtype )


def getrandomvegetarian(program):
    if program == "yes" and dietchooser == "specific diet" and userdecision == "vegetarian":
     print(vegetarian_name)
     print(vegetarian_instructions)
     #print(Ingredients)
     print(vegetarian_mealprice)
     #print(preptime)
     #print(cooktime)
     #print(summary)
     print(vegetarian_dishtype)
     print(vegetarian_servings)
     return (vegetarian_name, vegetarian_instructions, vegetarian_mealprice, vegetarian_servings,  vegetarian_dishtype )

def getrandomvgean(program):
    if program == "yes" and dietchooser == "specific diet" and userdecision == "vegan":
     print(vname)
     print(vinstructions)
     #print(Ingredients)
     print(vmealprice)
     #print(preptime)
     #print(cooktime)
     #print(summary)
     print(vdishtype)
     print(vservings)
     return (vname, vinstructions, vmealprice, vservings,  vdishtype ) 



while True:
    if program == "yes" and dietchooser == "randomized":
        print("\n")

        print(f"the name of your random dish is {name}")  

        print("\n")


        print(f"The dish type is a {dishtype}")

        print("\n")

        print("The instructions are as follows:")

        print("\n")

        print(f"{instructions}")

        print("\n")

        print(f"The amount of servings in this recipe is {servings} servings")

        print("\n")

        #print(f"The price of all the ingredients to reach max servings would be about ${mealprice} dollars")

        #print("\n")

        print("I hope you enjoy the recipe, good luck!")
        break
    elif program == "q":
        break

    elif program == "yes" and dietchooser == "specific diet" and userdecision == "vegetarian":
        print("\n")

        print(f"It is {veg_vegetarian} that your dish is vegetarian")

        print("\n")

        print(f"the name of your random dish is {vegetarian_name}")  

        print("\n")


        print(f"The dish type is a {vegetarian_dishtype}")

        print("\n")

        print("The instructions are as follows:")

        print("\n")

        print(f"{vegetarian_instructions}")

        print("\n")

        print(f"The amount of servings in this recipe is {vegetarian_servings} servings")

        print("\n")

        #print(f"The price of all the ingredients to reach max servings would be about ${mealprice} dollars")

        #print("\n")

        print("I hope you enjoy the recipe, good luck!")
        break

    elif program == "yes" and dietchooser == "specific diet" and userdecision == "vegan":
        print("\n")

        print(f"It is {vvegan} that your dish is vegan")

        print("\n")

        print(f"the name of your random dish is {vname}")  

        print("\n")


        print(f"The dish type is a {vdishtype}")

        print("\n")

        print("The instructions are as follows:")

        print("\n")

        print(f"{vinstructions}")

        print("\n")

        print(f"The amount of servings in this recipe is {vservings} servings")

        print("\n")

        #print(f"The price of all the ingredients to reach max servings would be about ${mealprice} dollars")

        #print("\n")

        print("I hope you enjoy the recipe, good luck!")
        break

    else:
        break
