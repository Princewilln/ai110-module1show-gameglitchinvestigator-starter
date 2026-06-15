# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggetsed that the secret be cast back to int for a proper numeric comparison instead of converting guess to string. 

I verified it with pytest, I also did manual test by type in inputs to see if the behaviour would be out of scope but it did not. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I did not get any misleading suggestion, howver I denied the suggestion to fix and issue the AI suggested which i haven't reviewd yet.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I reran the app.py and confirmed the behavior which I noticed intially was gone after severl testing

- Describe at least one test you ran (manual or using pytest)  
and what it showed you about your code.

I tested for out of range inputs and it will give me an error that my guess in out of range of the selected difficulty

- Did AI help you design or understand any tests? How?

yes AI helped provide some solution to my question after reviewing the function and the code line I provided and the it offered to fix it, which I accepted after proper review

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I don't quit understa this question but I will tell the friend to use up arrow to pull prevous commands and rerun streamlit run app.py. I will let the know the sessions terminate each time the use ctrl c and the have to rerun "streamlit run app.py" to up the app.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Reading and using AI explanation to better understand the propblem my code could be failing. 

  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Yes, and it actully teaches you how to prompt AI properly and not blindly pasting code errors

- What is one thing you would do differently next time you work with AI on a coding task?
i would start my project on time, knowing that working with AI does not elimate the human factor of manual review, which takes time.

- In one or two sentences, describe how this project changed the way you think about AI generated 
code.
AI do make mistake and we have to be in the loop to review and iclude our human insights.
