################################################
#
#
#
#############################################
#Define function to add movies to the movies list
def add_movie(num_to_add):
    #create loop based on user input of how many movies they want to add
    for i in range (0, num_to_add, 1):
        #Ask user for input on the movie title
        movie_title= input("Please enter the movie name: ")
        #Ask user for input on the movie budget
        movie_budget= int(input("Please enter the movie budget: "))
        #Create new movie tuple containing the entered title and budget
        new_movie = (movie_title, movie_budget)
        #Append movies list with the new_movie tuple
        movies.append(new_movie)
    return()
#Define function to solve for the average budget of movies
def budget_average():
    total_budgets = 0
    #create loop to add up budget of all movies
    for i in range (0, len(movies), 1):
        total_budgets += movies[i][1]

    average_budget = total_budgets/len(movies)
    return(average_budget)

def budget_sort():
    sort_control=0
    while(sort_control<=3):
        for i in range(1, len(movies), 1):
            holder = 0
            if i < len(movies):
                if movies[i][1] > movies[i-1][1]:
                    holder = movies[i]
                    movies[i] = movies[i-1]
                    movies[i-1] = holder
        sort_control+=1
    for i in range (0, len(movies), 1):
     print(f"{movies[i][0]}: ${movies[i][1]:,.2f}")
def high_budget(average):
    high_budget_movies = []
    for i in range(0, len(movies), 1):
        if movies[i][1] > average:
            overage = movies[i][1]-average
            holder = (movies[i][0], movies[i][1], overage)
            high_budget_movies.append(holder)
    return(high_budget_movies)

#Define movies list at beginning state
movies = [
    ("Interstellar", 165000000),
    ("The Dark Knight", 185000000),
    ("Inception", 160000000),
    ("Titanic", 200000000),
    ("Avengers: Infinity War", 316000000),
    ("Frozen II", 150000000),
    ("Joker", 55000000)
]
#print prompt asking for how many movies would like to be added.
num_to_add = int(input("How many movies would you like to add?: "))
add_movie(num_to_add)
average = budget_average()
print(f"Average Budget: ${average:,.2f}")

print("Movies with Budgets Higher Than Average:")
high_budget_movies = high_budget(average)
for i in range (0, len(high_budget_movies), 1):
    print(f"{high_budget_movies[i][0]}: ${high_budget_movies[i][1]:,.2f} (Higher by ${high_budget_movies[i][2]:,.2f})")
print("Total High-Budget Movies: ", len(high_budget_movies))
budget_sort()





