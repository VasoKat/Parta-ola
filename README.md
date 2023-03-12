# Parta-ola
Parta ola Game in Python
"Parta ola" is a retro game of chance played with one spin (or roulette). By spinning the wheel 
(or spinning the roulette wheel) we get one of the following six outcomes: "put one", "put two", "put all",
"take one", "take two", "take all". The game is played with two or more players. At the beginning of the
game each player has the same number of beans. The game is played in rounds. At the beginning of each
round, each player places one bean in the center of the table.Then
the player who has turn, spins the wheel and executes the resulting command. For example, even if the
next player is player B and this player brings “put one”. Player B then puts a bean in the
center of the table. Then the next player in line, i.e. C,
spins and executes the command, then the next player (i.e. D) plays, and so on.
The required actions for each spin order are as follows:
• “put one”: the player who brings “put one” must put a bean in the center of the table. If
has no beans left, then the player is eliminated from the game.
• “put two”: the player who brings “put two” must put two beans in the center of the table.
If he has nothing to do, then the player is excluded from the continuation of the game.
• “put all”: if a player brings “put all”, then all players must put a bean
in the center of the table. If a player does not have anything to put, then the player is eliminated from the game
continuation of the game.
• “take one”: the player who brings “take one” takes a bean from the center of the table. If that
was the last bean in the center of the table, then the round ends.
• “take two”: the player who brings “take two” takes two beans from the center of the table. If at
center there was only one bean, then it takes only one. If after this, there are no beans left
in the center, then the round ends.
• “take all”: the player who brings “take all” takes all the beans from the center of the table.
The round ends.
A player who is excluded from the continuation of the game is not eligible to participate in the same game again
 or in subsequent rounds. So the player loses. If all but one player loses, then the player
who remains is declared the winner and the game ends.
As soon as one round ends (because there are no beans left in the center), the next one begins
and all remaining players must participate by placing a bean in the center. If one
player does not have to put, then he is excluded from the continuation of the game. The player who plays first
in the new round is the next (not eliminated) to the one who played last in the previous round.