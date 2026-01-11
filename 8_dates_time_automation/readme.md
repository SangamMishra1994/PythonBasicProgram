# Dates, Time & Automation

## Focus: Importing modules (datetime, time) and working with real-world time

<details>
  <summary>1. Age Calculator</summary>
  <p><strong>Concept:</strong> Ask the user for their birth date (year, month, day).
     Calculate exactly how many years, months, and days old they are today.</p>
  <p><strong>Key Skill:</strong> The <code>datetime</code> module and subtracting dates (deltas).</p>
</details>

<details>
  <summary>2. Countdown Timer</summary>
  <p><strong>Concept:</strong> Ask the user for a time in seconds (e.g., 10). The program waits for that amount of time, printing the remaining seconds every second, and then prints "Time's up!"</p>
  <p><strong>Key Skill:</strong> <code>time.sleep()</code> and while loops.</p>
</details>

<details>
  <summary>3. Digital Clock</summary>
  <p><strong>Concept:</strong> Create a loop that prints the current time, waits one second, clears the screen, and prints the new time again to simulate a digital clock.</p>
  <p><strong>Key Skill:</strong> Infinite loops and refreshing terminal output.</p>
</details>

<hr>

<h3>Category 2: File Handling (Input/Output)</h3>
<p><strong>Focus:</strong> Reading from and writing to text files (.txt).</p>

<details>
  <summary>4. Personal Journal / Diary</summary>
  <p><strong>Concept:</strong> The user types a diary entry. The program saves it to a file named <code>diary.txt</code> with the current timestamp automatically added at the top.</p>
  <p><strong>Key Skill:</strong> File appending (<code>open('file.txt', 'a')</code>) and string formatting.</p>
</details>

<details>
  <summary>5. High Score Tracker</summary>
  <p><strong>Concept:</strong> Ask the user for a game score. Check a file named <code>highscore.txt</code>. If the new score is higher than the one in the file, overwrite it; otherwise, notify the user.</p>
  <p><strong>Key Skill:</strong> Reading files (<code>'r'</code>), type conversion, and conditional writing.</p>
</details>

<details>
  <summary>6. Quiz Maker (From File)</summary>
  <p><strong>Concept:</strong> Write questions and answers in a text file (e.g., <code>question,answer</code>). The program reads the file line-by-line and quizzes the user.</p>
  <p><strong>Key Skill:</strong> Parsing strings (splitting lines by commas).</p>
</details>

<hr>

<h3>Category 3: Logic & Algorithms</h3>
<p><strong>Focus:</strong> Thinking like a programmer.</p>

<details>
  <summary>7. Prime Number Checker</summary>
  <p><strong>Concept:</strong> The user enters a number, and the program determines if it is a Prime Number.</p>
  <p><strong>Key Skill:</strong> Modulo operator (%) and for loops with <code>break</code>.</p>
</details>

<details>
  <summary>8. Caesar Cipher (Simple Encryption)</summary>
  <p><strong>Concept:</strong> The user enters a message and a shift number. Each letter is shifted to create a secret code.</p>
  <p><strong>Key Skill:</strong> <code>ord()</code> and <code>chr()</code> functions.</p>
</details>

<details>
  <summary>9. ASCII Pattern Printer</summary>
  <p><strong>Concept:</strong> Ask the user for a number and print a pyramid or diamond of stars.</p>
  <pre>
  *
 ***
*****
  </pre>
  <p><strong>Key Skill:</strong> Nested loops and string multiplication.</p>
</details>

<details>
  <summary>10. Factorial Finder</summary>
  <p><strong>Concept:</strong> Calculate the factorial of a number (e.g., 5! = 120).</p>
  <p><strong>Key Skill:</strong> Recursion or for loops.</p>
</details>

<hr>

<h3>Category 4: Enhanced String Manipulation</h3>

<details>
  <summary>11. Email Slicer</summary>
  <p><strong>Concept:</strong> Extract username and domain from an email address.</p>
  <p><strong>Key Skill:</strong> String slicing using the <code>@</code> symbol.</p>
</details>

<details>
  <summary>12. Morse Code Translator</summary>
  <p><strong>Concept:</strong> Convert text into Morse Code dots and dashes.</p>
  <p><strong>Key Skill:</strong> Dictionaries for character mapping.</p>
</details>

<hr>

<h3>Category 5: Mini-Systems (Class/Object Concepts)</h3>

<details>
  <summary>13. Simple ATM Simulator</summary>
  <p><strong>Concept:</strong> Menu-driven ATM with balance checking, deposit, and withdrawal.</p>
  <p><strong>Key Skill:</strong> Variables or basic classes and input validation.</p>
</details>

<details>
  <summary>14. Login System</summary>
  <p><strong>Concept:</strong> Stored username/password with 3 login attempts.</p>
  <p><strong>Key Skill:</strong> While loops with counters.</p>
</details>

<details>
  <summary>15. Hangman Game</summary>
  <p><strong>Concept:</strong> Guess letters of a hidden word with limited lives.</p>
  <p><strong>Key Skill:</strong> List checking and state tracking.</p>
</details>
