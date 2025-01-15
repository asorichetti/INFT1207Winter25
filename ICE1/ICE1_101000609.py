################################################
# Author: Alex Sorichetti
# Student ID: 101000609
# Description: Code to analyze movie budgets and save results to a file
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
#Define function to sort movies by budget from highest to lowest
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
#Define function to find movies with budgets above the average
def high_budget(average):
    high_budget_movies = []
    for i in range(0, len(movies), 1):
        if movies[i][1] > average:
            overage = movies[i][1]-average
            holder = (movies[i][0], movies[i][1], overage)
            high_budget_movies.append(holder)
    return(high_budget_movies)
#Define function to read movie titles and budget from a text file
def read_file(file_name):
    movies = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            name, budget = line.strip().split(", ")
            movies.append((name, int(budget)))
    return movies
#Define function to write results of program to an output file
def write_output_file(file_name, average_budget, high_budget_movies):
    with open (file_name, "w") as file:
        file.write(f"Average Budget: ${average_budget:,.2f}\n")
        file.write("Movies with Budgets Higher than the Average Budget:\n")
        for i in range (0, len(high_budget_movies), 1):
            file.write(f"{high_budget_movies[i][0]}: ${high_budget_movies[i][1]:,}\n")

#Call for read_file function to bring in starting movie list
movies = read_file("ICE1/MovieList.txt")
#print prompt asking for how many movies would like to be added.
num_to_add = int(input("How many movies would you like to add?: "))
#Send user input to function to add movies
add_movie(num_to_add)
#Call function to solve for average budget of movies and store result in variable average
average = budget_average()
#Display average
print(f"Average Budget: ${average:,.2f}")

print("Movies with Budgets Higher Than Average:")
#Call for function to solve for movies with budgets greater than average and store result in variable high_budget_movies
high_budget_movies = high_budget(average)
#print all movies stored in high_budget_movies
for i in range (0, len(high_budget_movies), 1):
    print(f"{high_budget_movies[i][0]}: ${high_budget_movies[i][1]:,.2f} (Higher by ${high_budget_movies[i][2]:,.2f})")
#print the total number of high budget movies
print("Total High-Budget Movies: ", len(high_budget_movies))
#Call function to sort movies by budget
budget_sort()
#Write results of program to output file and print message informing this has been done
write_output_file("ICE1\Output.txt", average, high_budget_movies)
print("\nResults saved to 'Output.txt'")





