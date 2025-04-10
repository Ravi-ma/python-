from flask import Flask, render_template, request
import random

# Initialize Flask app
app = Flask(__name__)

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

# Define some flashcards and decks
def setup_flashcards():
    user_name = "Student"
    trainer = FlashcardTrainer(user_name)

    # Deck: Country Capitals
    country_capitals = Deck("Country Capitals")
    country_capitals.add_card(Flashcard("What is the capital of France?", ["Paris", "Berlin", "Rome", "Madrid"], "Paris", "It's also known as the City of Light."))
    country_capitals.add_card(Flashcard("What is the capital of Germany?", ["Vienna", "Berlin", "Zurich", "Brussels"], "Berlin", "It was divided during the Cold War."))
    trainer.add_deck(country_capitals)

    # Deck: Animals
    animals = Deck("Animals")
    animals.add_card(Flashcard("Which animal is known as the king of the jungle?", ["Lion", "Tiger", "Elephant", "Giraffe"], "Lion", "It's a big cat."))
    animals.add_card(Flashcard("Which animal is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], "Blue Whale", "It lives in the ocean."))
    trainer.add_deck(animals)

    return trainer

@app.route('/')
def home():
    return "Welcome to the Flashcard App! Visit /quiz to start a quiz."

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    trainer = setup_flashcards()
    trainer.select_deck("Country Capitals")  # Example: Selecting Country Capitals deck
    trainer.start_quiz()

    return "Quiz Finished! Check the terminal for results."

# Start the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
