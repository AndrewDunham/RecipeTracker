import json

def submitRecipe(data, fileName="Recipes.json"):
    with open(fileName, "w") as file:
        json.dump(data, file, indent=4)


def newRecipe():
    with open('Recipes.json') as jsonFile:
        data = json.load(jsonFile)

        moreFood = data['Recipes']

        #Get the last recipe's ID and add one
        ###NEEDS A CONDITION IF THERE ISN'T ANY 0 element
        RecipeID = (moreFood[-1]['RecipeID']) + 1

        newRecipe = {
            "RecipeID":RecipeID,
            "RecipeName":"",
            "Description":"",
            "DateCreated":"",
            "LastMade":"",
            "Steps":[""],
            "Details":{
                "Prep":"",
                "Cook":"",
                "Total":"",
                "Servings":""
                },
                "ImageURL":""
            }

        moreFood.append(newRecipe)
    submitRecipe(data)



newRecipe()
