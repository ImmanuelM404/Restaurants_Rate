# with open('scores.txt') as s:
#     lines = s.readlines()


"""Restaurant rating lister."""


# put your code here

def get_scores():
    
    score_file = open('scores.txt')

    scores = {}

    for lines in score_file:
        restaurant, score = lines.strip().split(':')
        scores[restaurant] = int(score)
    return scores

def add_restaurant(scores):
    print("Please add a rating for your favorite restaurant!")
    restaurant = input("Restaurant name> ")
    rating = int(input("Rating> "))

    scores[restaurant] = rating

def add_new_rating(scores):
     for restaurant, rating in sorted(scores.items()):
        print(restaurant, " is rated at ", rating, ".", sep='')

scores = get_scores()

add_restaurant(scores)

add_new_rating(scores)



# restaurant_rating = {}
# new_rest = input("Enter restaurant name: ")
# new_rest_rate = input("Leave a rating: ")
# if new_rest_rate.isdigit():
#     new_rest_rate = int(new_rest_rate)
# else:
#     print("Please enter a number for rating")
#     quit()
# print(new_rest , ":" , new_rest_rate)
# new_input = new_rest , ":" , new_rest_rate

# restaurant_rating[] 

# with open('scores.txt') as s:
#     for line in s: 
#         (key, value)= line.strip().split(':')

#         restaurant_rating[str(key)] = value
# for k, v in sorted(restaurant_rating.items()):
#     print(k, " is rated at ", v, '.', sep="")

# print(restaurant_rating)
    
# s.close()