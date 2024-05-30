with open("movies.txt", "w") as file:
    file.write("Cat on the Hot Tin Roof\nOn the Waterfront\nMonty Python and the Holy Grail\n")

def populate_list(file_name):
    movie_list = []
    with open(file_name, "r") as file:
        for line in file:
            movie_list.append(line.strip())
    return movie_list

def display_menu():
    print("\nMovie list menu")
    print("list --> Display movie titles.")
    print("add --> Add a movie title")
    print("delete --> Delete a movie title")
    print("exit --> Exit the application")
    
def display_titles(movie_list):
    print("\nMovie Titles:")
    for idx, title in enumerate(movie_list, start=1):
        print(f"{idx}. {title}")
        
def add_title(movie_list, title, file_name):
    movie_list.append(title)
    with open(file_name, "a") as file:
        file.write(title + "\n")
    print(f"\n{title} has been added to the list")
    
def delete_title(movie_list, index, file_name):
    if 1 <= len(movie_list):
        deleted_title = movie_list.pop(index - 1)
        with open(file_name, "w") as file:
            file.write["\n".join(movie_list)]
        print(f"\n {deleted_title} has been deleted from the list")
    else:
        print(f"\nInvalid index number. No movie was deleted")
        
def main():
    movie_file = "movie.txt"
    movie_list = populate_list(movie_file)
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "list":
            display_titles(movie_list)
        elif choice == "add":
            new_title = input("Enter the new movie title:")
            add_title(movie_list, new_title, movie_file)
            display_titles(movie_list)
        elif choice == "delete":
            display_titles(movie_list)
            index = int(input("Enter the number of the movie title you would delete:"))
            delete_title(movie_list, index, movie_file)
            display_titles(movie_list)
        elif choice == "exit":
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again")
            
if __name__ == "__main__":
    main()