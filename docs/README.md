## Docs on using discord.py

Use the code to write the docs
```
@client.command(aliases=['toss'])
async def coinflip(ctx, *, question):
    """ aliases takes a list of strings. You can have +1 aliases.
        * allows for multiple arguments to be passed
    """
    responses = ['heads', 'tails']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}\n{ctx.author.mention}')
```
