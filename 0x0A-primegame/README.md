<h1>0x0A. Prime Game</h1>

<strong>Algorithm Python</strong><br>

<p>For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.</p>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>Prime Numbers</strong>:</p>

<ul>
<li>Understanding what prime numbers are.</li>
<li>Efficient algorithms for identifying prime numbers within a range.</li>
</ul></li>
<li><p><strong>Sieve of Eratosthenes</strong>:</p>

<ul>
<li>An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.</li>
</ul></li>
<li><p><strong>Game Theory</strong>:</p>

<ul>
<li>Basic principles of competitive games where players take turns and the concept of optimal play.</li>
<li>Understanding win conditions and strategies that lead to a win or loss.</li>
</ul></li>
<li><p><strong>Dynamic Programming/Memoization</strong>:</p>

<ul>
<li>Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.</li>
</ul></li>
<li><p><strong>Python Programming</strong>:</p>

<ul>
<li>Loops and conditional statements for implementing game logic and algorithms.</li>
<li>Arrays and lists for storing the integers and tracking removed numbers.</li>
</ul></li>
</ol>

<h3>Resources:</h3>

<ul>
<li><p><strong>Prime Numbers and Sieve of Eratosthenes</strong>:</p>

<ul>
<li><a href="/https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers" title="Khan Academy: Prime Numbers" target="_blank">Khan Academy: Prime Numbers</a>: Introduction to prime numbers.</li>
<li><a href="/https://www.geeksforgeeks.org/sieve-of-eratosthenes/" title="Sieve of Eratosthenes in Python" target="_blank">Sieve of Eratosthenes in Python</a>: A step-by-step guide to implementing the sieve algorithm in Python.</li>
</ul></li>
<li><p><strong>Game Theory Basics</strong>:</p>

<ul>
<li><a href="/https://www.investopedia.com/terms/g/gametheory.asp" title="Game Theory Introduction" target="_blank">Game Theory Introduction</a>: A simple explanation of game theory and strategic decision-making.</li>
</ul></li>
<li><p><strong>Dynamic Programming</strong>:</p>

<ul>
<li><a href="/https://skerritt.blog/dynamic-programming/" title="What Is Dynamic Programming With Python Examples" target="_blank">What Is Dynamic Programming With Python Examples</a>: An introduction to dynamic programming with Python examples.</li>
</ul></li>
<li><p><strong>Python Official Documentation</strong>:</p>

<ul>
<li><a href="/https://docs.python.org/3/tutorial/introduction.html#lists" title="Python Lists" target="_blank">Python Lists</a>: Managing lists in Python, useful for tracking the game state.</li>
</ul></li>
</ul>

<p>By grasping these concepts and making use of the recommended resources, you will be well-equipped to approach the problem with a solid understanding of both the mathematical and programming challenges involved. The key to success in this project lies in applying efficient algorithms to manage the game&rsquo;s state and making optimal decisions based on the game&rsquo;s rules.</p>

<h2>Additional Resources</h2>

<ul>
<li><a href="/https://www.youtube.com/watch?v=Jw2pniZCLi8" title="Mock Technical Interview" target="_blank">Mock Technical Interview</a></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.x)</li>
<li>All your files must be executable</li>
</ul>

<p>Maria and Ben are playing a game. Given a set of consecutive integers starting from <code>1</code> up to and including <code>n</code>, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.</p>

<p>They play <code>x</code> rounds of the game, where <code>n</code> may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.</p>

<ul>
<li>Prototype: <code>def isWinner(x, nums)</code></li>
<li>where <code>x</code> is the number of rounds and <code>nums</code> is an array of <code>n</code> </li>
<li>Return: name of the player that won the most rounds</li>
<li>If the winner cannot be determined, return <code>None</code></li>
<li>You can assume <code>n</code> and <code>x</code> will not be larger than 10000</li>
<li>You cannot import any packages in this task</li>
</ul>

<p>Example:</p>

<ul>
<li><code>x</code> = <code>3</code>, <code>nums</code> = <code>[4, 5, 1]</code></li>
</ul>

<p>First round: <code>4</code></p>

<ul>
<li>Maria picks 2 and removes 2, 4, leaving 1, 3</li>
<li>Ben picks 3 and removes 3, leaving 1</li>
<li>Ben wins because there are no prime numbers left for Maria to choose</li>
</ul>

<p>Second round: <code>5</code></p>

<ul>
<li>Maria picks 2 and removes 2, 4, leaving 1, 3, 5</li>
<li>Ben picks 3 and removes 3, leaving 1, 5</li>
<li>Maria picks 5 and removes 5, leaving 1</li>
<li>Maria wins because there are no prime numbers left for Ben to choose</li>
</ul>

<p>Third round: <code>1</code></p>

<ul>
<li>Ben wins because there are no prime numbers for Maria to choose</li>
</ul>

<p><strong>Result: Ben has the most wins</strong></p>

<pre><code>carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__(&#39;0-prime_game&#39;).isWinner


print(&quot;Winner: {}&quot;.format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$
</code></pre>

<pre><code>carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
</code></pre>
