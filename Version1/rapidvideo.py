import pyppeteer as p

async def main():
    browser = await p.launch()
    page = await browser.newPage()

    page.goto('https://there.to/v/dk7epcxw-5572g8')

    page.click('.fakeplaybutton')


import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
result = loop.run_until_complete(main())