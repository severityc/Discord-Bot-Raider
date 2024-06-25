import discord
import asyncio

def read_tokens():
    with open("tokens.txt", "r") as file:
        tokens = [line.strip() for line in file]
    return tokens

async def send_message_with_bot(token, channel_id, message, count):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        channel = client.get_channel(channel_id)
        if channel is None:
            print(f"Channel ID {channel_id} not found.")
            await client.close()
            return
        for _ in range(count):
            await channel.send(message)
        await client.close()

    try:
        await client.start(token)
    except discord.LoginFailure:
        print(f"Failed to login with token: {token}")

async def main():
    tokens = read_tokens()
    channel_id = int(input("Enter the Channel ID: "))
    message = input("Enter the message to send: ")
    count = int(input("Enter the number of times to send the message: "))

    tasks = [send_message_with_bot(token, channel_id, message, count) for token in tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
