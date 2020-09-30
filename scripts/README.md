## I don't like magic.

* Do not use third party libraries.
> One should stay away from third party libraries as much as possible.
    Every function in the bot should stick with python's standard library as 
    much as possible - which is always. 

* Security comes first.  
> If using a third party library reduces the risk of implementing it yourself,
    then the use of third party libraries is encouraged.

Besides discord.py, there shouldn't be any other dependencies. 

The point of this bot is to use it as a learning experience. Whatever function
you would like to add to the bot, create a script for using python's standard
library and get it to work. Once it is working, then the code can be implemented
in the main script. 
If you are using third party libraries, you are learning to cobble together 
what other people have done. 
