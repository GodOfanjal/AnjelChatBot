import os

API_KEY = os.getenv('API_KEY')

on_message(filters.command(["start", f"start@{U}"]))
async def repo(_, message):
    await message.reply_text("irukan")    

    bot.pulling()

    await bot.start()
    print(
        """
-----------------
| bot Started! |
-----------------
"""
    )
    await idle()

loop = get_event_loop()
loop.run_until_complete(main())





