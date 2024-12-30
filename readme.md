### README: Rock, Paper, Scissors Game  

---

#### **Project Title**: Rock, Paper, Scissors Game  

---

#### **Description**:  
This is a simple Python-based implementation of the classic game "Rock, Paper, Scissors." The user competes against the computer by choosing one of the three options (rock, paper, or scissors), and the computer randomly selects its choice. The game keeps track of the number of wins for both the user and the computer, and the user can exit the game at any time.

---

#### **Features**:  
- **Interactive Gameplay**: Users can choose their options and compete with the computer.  
- **Randomized Computer Choices**: The computer's choice is generated randomly for fairness.  
- **Score Tracking**: The program keeps a running tally of wins for both the user and the computer.  
- **Quit Option**: The user can exit the game anytime by typing "Q".  

---

#### **How to Play**:  
1. Run the script in a Python environment.  
2. Follow the prompts to type "rock," "paper," or "scissors" to play the game.  
3. To exit the game, type "Q" (case-insensitive).  
4. The program will display who won each round and keep track of the scores.  
5. At the end of the game, the total scores for both the user and the computer will be displayed.  

---

#### **Rules of the Game**:  
- **Rock beats Scissors.**  
- **Scissors beat Paper.**  
- **Paper beats Rock.**  
- If both the user and the computer make the same choice, it's a tie (not explicitly shown in this code but inferred).  

---

#### **Example Gameplay**:  
```plaintext
Type Rock/Paper/Scissors or Q to quit: rock  
Computer picked paper.  
You lost!  

Type Rock/Paper/Scissors or Q to quit: scissors  
Computer picked paper.  
You won!  

Type Rock/Paper/Scissors or Q to quit: q  
You won 1 times.  
The computer won 1 times.  
Goodbye!
```

---

#### **Code Highlights**:  
- **Randomization**: The `random` module ensures the computer's choice is unpredictable.  
- **Input Handling**: The program processes user input and checks for valid options.  
- **Conditionals**: The core logic uses `if-elif-else` statements to determine the winner of each round.  
- **Counters**: Two counters (`user_wins` and `computer_wins`) keep track of the respective scores.

---

#### **How to Run the Project**:  
1. Make sure Python is installed on your system.  
2. Save the code in a `.py` file (e.g., `rock_paper_scissors.py`).  
3. Open a terminal or command prompt and run the script:  
   ```bash
   python rock_paper_scissors.py
   ```
4. Enjoy playing the game!

---

#### **Potential Enhancements**:  
- Add a tie counter to track tied rounds.  
- Allow users to set the number of rounds to play before ending the game.  
- Implement a graphical user interface (GUI) for a more interactive experience.  
- Include additional options, such as "Lizard" and "Spock" (from the extended version of the game).  

---

#### **Author**:  
Akinyemi Taiwo  


Feel free to share, modify, and play! 