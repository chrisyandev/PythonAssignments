import asyncio
import aiohttp


class HttpRequest:

    @classmethod
    async def get_pokedex_data(cls, id_, url: str, session: aiohttp.ClientSession,) -> dict:
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
    async def process_requests(cls, requests: list) -> list:
        """
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
        :param requests: a list of int's
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        async with aiohttp.ClientSession() as session:
            print("***process_requests")
            async_coroutines = [cls.get_pokedex_data(id_, url, session)
                                for id_ in requests]

            responses = await asyncio.gather(*async_coroutines)

            # for response in responses:
            #     print(response)
            return responses