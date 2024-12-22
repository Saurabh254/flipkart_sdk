import asyncio

import aiohttp


class RequestHandler:
    def __init__(self, product_name: str) -> None:
        self.base_url = "https://www.flipkart.com/search"
        self.product_name = product_name

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()

    async def make_request(self) -> str:
        params = {"q": self.product_name}
        async with self._session.get(self.base_url, params=params) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise Exception(
                    f"Failed with status code: {response.status}, {(await response.text())[:40]}"
                )


if __name__ == "__main__":

    async def main():
        async with RequestHandler(product_name="iphone 16 pro max") as request_handler:
            response = await request_handler.make_request()
            print(response)

    asyncio.run(main())
