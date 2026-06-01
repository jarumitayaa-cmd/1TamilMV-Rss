import asyncio
from aiohttp import web, ClientSession
from pyrogram import Client, idle
from configs import API_ID, API_HASH, BOT_TOKEN, PORT, URL, SCRAPE_INTERVAL, PING_INTERVAL
from tamilmv import tmv_scraper

# Initialize as a Bot Account with in_memory=True to bypass file generation/cache crashes
User = Client(
    "User", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
    in_memory=True
)

# ---------- Async Keep-alive Ping ----------
async def ping_loop():
    """Asynchronously pings the web server link to keep the container awake."""
    await asyncio.sleep(10)  # Give the server a few seconds to boot up first
    async with ClientSession() as session:
        while True:
            try:
                async with session.get(URL, timeout=30) as response:
                    if response.status == 200:
                        print("🍁 Ping successful")
                    else:
                        print(f"👹 Ping failed: {response.status}")
            except Exception as e:
                print(f"❌ Ping exception: {e}")
            await asyncio.sleep(PING_INTERVAL)

# ---------- TamilMV Scraper Loop ----------
async def main_loop():
    """Background task handling the continuous RSS scraping."""
    while True:
        print("🌀 Starting TamilMV scraping...")
        try:
            await tmv_scraper(User)
        except Exception as e:
            print(f"❌ Scraper encountered an error: {e}")
        await asyncio.sleep(SCRAPE_INTERVAL)

# ---------- Web server ----------
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root(request):
    return web.json_response("TamilMV RSS running ✅")

async def start_server():
    app = web.Application(client_max_size=30_000_000)
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"🌐 Web server running internally on port {PORT}")

# ---------- Startup ----------
async def start_bot():
    # Start Pyrogram Bot
    await User.start()
    bot_me = await User.get_me()
    print(f"✅ Bot logged in: @{bot_me.username}")
    
    # Start Web Server
    await start_server()
    
    # Register Background Tasks safely inside the asyncio event loop
    asyncio.create_task(main_loop())
    asyncio.create_task(ping_loop())
    
    # Keep application alive
    await idle()
    await User.stop()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("🛑 Bot stopped manually.")
