# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of this game is to guess a secret number 
- [ ] Detail which bugs you found.
I found that the hint does not direct the player towards right direction on the number line, for example if the secret is 90 and you guessed 8, it tells you to go lower as oppose to going higher

On the left pain the difficulty attempts where assigned backwards, easy difficulty is suppose to have more attempts that normal and hard.

attempts left starts with -1 of the total attempts

The game specified a range 1 - 100, but it accepts number higher than 100 or lesser than 1 and hints you to go lower when you type a number less than one, and to go higher when you type a number higher than 100

When the dificulty is changed the range of input does not change to match the range defined for the leve of difficulty.

- [ ] Explain what fixes you applied.
guess > secret → the guess is too high → tell the player to go LOWER insted of go HIGHER it had prior
guess < secret (the else) → the guess is too low → tell the player to go HIGHER instead of go LOWER it had prior.

Fixed. Easy now gets 10 attempts, Normal 7, Hard 5 — a clean descending order that matches the difficulty intent. Also notice the file now has a new FIXME on line 98 (attempts initialized to 1 instead of 0). 

change attempt state to be = 0, instead of 1, so that way the program start with the complete attempts.

fix the Enter your guess: not to accept inputs that are out of range. parse_guess now accepts low and high and rejects any guess outside th
at range with a clear error message

Fixed. Now the displayed range will dynamically update — Easy shows "1 and 20", Normal "1 and 100", Hard "1 and 50" — matching what the game actually uses.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
