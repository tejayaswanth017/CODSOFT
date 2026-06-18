movies = {
    "action": ["John Wick", "Mad Max", "The Dark Knight"],
    "comedy": ["The Hangover", "Superbad", "21 Jump Street"],
    "horror": ["The Conjuring", "Insidious", "Annabelle"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"],
    "sports": ["MS Dhoni", "83", "Chak De India"]
}

print("========== Movie Recommendation System ==========")

while True:
    print("\nAvailable categories:")
    for category in movies:
        print("-", category)

    choice = input("\nEnter your favorite category (or 'exit' to quit): ").lower()

    if choice == "exit":
        print("Thank you for using the Recommendation System!")
        break

    if choice in movies:
        print("\nRecommended Movies:")
        for movie in movies[choice]:
            print("-", movie)
    else:
        print("Category not found. Try again.")