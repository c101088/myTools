# encoding: utf-8
# Author    : clz
# Datetime  : 2020/7/24 22:01
# User      : Administrator
# Product   : PyCharm
# Project   : pythonReptile
# File      : test.py
# explain   : 文件说明


import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://rsj.ningbo.gov.cn/col/col1229114380/index.html')
    # await page.screenshot({'path': 'example.png'})
    dimensions = await page.evaluate('''() => {
        return {
            width: document.getElementById('6030800'),
        }
    }''')
    print(dimensions)
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())