import random

class Flashcard:
    def __init__(self, question, options, answer, hint):
        self.question = question
        self.options = options
        self.answer = answer
        self.hint = hint
        self.history = []

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

class FlashcardTrainer:
    def __init__(self, user_name):
        self.user_name = user_name
        self.decks = {}
        self.current_deck = None
        self.score = 0

    def add_deck(self, deck):
        self.decks[deck.name] = deck

    def select_deck(self, deck_name):
        if deck_name in self.decks:
            self.current_deck = self.decks[deck_name]
        else:
            print(f"No deck named {deck_name} found.")

    def show_hint(self, card):
        print(f"Hint: {card.hint}")

    def start_quiz(self):
        if not self.current_deck:
            print("No deck selected.")
            return
        
        print(f"Starting quiz on {self.current_deck.name}")
        wrong_answers = []

        for card in self.current_deck.cards:
            print(f"\nQuestion: {card.question}")
            for idx, option in enumerate(card.options, 1):
                print(f"{idx}. {option}")
            
            show_hint = input("Do you want a hint? (yes/no): ").strip().lower()
            if show_hint == "yes":
                self.show_hint(card)

            answer = int(input("Your answer (choose the option number): ").strip())
            if card.options[answer - 1] == card.answer:
                print("Correct!")
                self.score += 1
                card.history.append(True)
            else:
                print(f"Wrong. The correct answer is {card.answer}.")
                card.history.append(False)
                wrong_answers.append(card)

        self.review_wrong_answers(wrong_answers)
        print(f"\nQuiz finished! Your score: {self.score}/{len(self.current_deck.cards)}")

    def review_wrong_answers(self, wrong_answers):
        if not wrong_answers:
            return
        
        print("\nReviewing wrong answers...")
        for card in wrong_answers:
            print(f"\nQuestion: {card.question}")
            for idx, option in enumerate(card.options, 1):
                print(f"{idx}. {option}")
            
            answer = int(input("Your answer (choose the option number): ").strip())
            if card.options[answer - 1] == card.answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is {card.answer}.")

def main():
    user_name = input("Enter your name: ").strip()
    trainer = FlashcardTrainer(user_name)

    country_capitals = Deck("Country Capitals")
    country_capitals.add_card(Flashcard("What is the capital of France?", ["Paris", "Berlin", "Rome", "Madrid"], "Paris", "It's also known as the City of Light."))
    country_capitals.add_card(Flashcard("What is the capital of Germany?", ["Vienna", "Berlin", "Zurich", "Brussels"], "Berlin", "It was divided during the Cold War."))
    country_capitals.add_card(Flashcard("What is the capital of Japan?", ["Beijing", "Seoul", "Tokyo", "Bangkok"], "Tokyo", "It's the largest city in Japan."))
    country_capitals.add_card(Flashcard("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa", "It is not the largest city in Canada."))
    country_capitals.add_card(Flashcard("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], "Canberra", "It's not the most famous city in Australia."))
    country_capitals.add_card(Flashcard("What is the capital of Italy?", ["Florence", "Venice", "Milan", "Rome"], "Rome", "It is home to the Colosseum."))
    country_capitals.add_card(Flashcard("What is the capital of Brazil?", ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"], "Brasilia", "It's a planned city developed in 1960."))

    animals = Deck("Animals")
    animals.add_card(Flashcard("Which animal is known as the king of the jungle?", ["Lion", "Tiger", "Elephant", "Giraffe"], "Lion", "It's a big cat."))
    animals.add_card(Flashcard("Which animal is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], "Blue Whale", "It lives in the ocean."))
    animals.add_card(Flashcard("Which bird is known for its colorful plumage?", ["Penguin", "Peacock", "Sparrow", "Ostrich"], "Peacock", "It has a fan-shaped tail."))
    animals.add_card(Flashcard("Which animal is known for its trunk?", ["Elephant", "Rhino", "Hippo", "Giraffe"], "Elephant", "It uses its trunk for drinking water."))
    animals.add_card(Flashcard("Which animal is the fastest land animal?", ["Cheetah", "Lion", "Horse", "Kangaroo"], "Cheetah", "It can run up to 75 mph."))
    animals.add_card(Flashcard("Which animal is known for its ability to change color?", ["Chameleon", "Frog", "Lizard", "Gecko"], "Chameleon", "It can blend into its surroundings."))
    animals.add_card(Flashcard("Which animal is the tallest in the world?", ["Elephant", "Giraffe", "Kangaroo", "Camel"], "Giraffe", "It has a very long neck."))

    trainer.add_deck(country_capitals)
    trainer.add_deck(animals)

    print("\nAvailable decks:")
    for deck_name in trainer.decks.keys():
        print(f"- {deck_name}")

    selected_deck = input("Select a deck: ").strip()
    trainer.select_deck(selected_deck)

    trainer.start_quiz()

if __name__ == "__main__":
    main()