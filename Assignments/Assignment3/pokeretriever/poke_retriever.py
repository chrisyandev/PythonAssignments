import asyncio
import aiohttp


class PokeRetriever:

    @classmethod
    def retrieve(cls, mode, ids: list):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(cls.process_requests(mode, ids))
        return response

    @staticmethod
    async def get_pokedex_data(id_, url: str, session: aiohttp.ClientSession,) -> dict:
        """
        :param id_: an int or str
        :param url: a string, the unformatted url (missing parameters)
        :param session: a HTTP session
        :return: a dict, json representation of response.
        """
        target_url = url.format(id_)
        response = await session.request(method="GET", url=target_url)
        # print("Response object from aiohttp:\n", response)
        # print("Response object type:\n", type(response))
        # print("-----")
        json_dict = await response.json()
        return json_dict

    @classmethod
    async def process_requests(cls, mode: str, ids: list) -> tuple:
        """
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
        :param mode: a str
        :param ids: a list of int or str
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "https://pokeapi.co/api/v2/%s/{}/" % mode
        async with aiohttp.ClientSession() as session:
            print("***process_requests")
            async_coroutines = [cls.get_pokedex_data(id_, url, session)
                                for id_ in ids]

            responses = await asyncio.gather(*async_coroutines)

            # for response in responses:
            #     print(response)
            return responses