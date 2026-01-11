# File Handling

<h3>Category 2: File Handling (Input/Output)</h3>
<p><strong>Focus:</strong> Reading from and writing to text files (.txt).</p>

<details>
  <summary>1. Personal Journal / Diary</summary>
  <p><strong>Concept:</strong> The user types a diary entry. The program saves it to a file named <code>diary.txt</code> with the current timestamp automatically added at the top.</p>
  <p><strong>Key Skill:</strong> File appending (<code>open('file.txt', 'a')</code>) and string formatting.</p>
</details>

<details>
  <summary>2. High Score Tracker</summary>
  <p><strong>Concept:</strong> Ask the user for a game score. Check a file named <code>highscore.txt</code>. If the new score is higher than the one in the file, overwrite it; otherwise, notify the user.</p>
  <p><strong>Key Skill:</strong> Reading files (<code>'r'</code>), type conversion, and conditional writing.</p>
</details>

<details>
  <summary>3. Quiz Maker (From File)</summary>
  <p><strong>Concept:</strong> Write questions and answers in a text file (e.g., <code>question,answer</code>). The program reads the file line-by-line and quizzes the user.</p>
  <p><strong>Key Skill:</strong> Parsing strings (splitting lines by commas).</p>
</details>
