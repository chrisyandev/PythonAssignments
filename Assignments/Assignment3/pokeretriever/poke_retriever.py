import asyncio
import aiohttp


class PokeRetriever:
    """ Contains methods to retrieve data from pokeapi. """

    @staticmethod
    async def get_pokedex_data(id_, url: str, session: aiohttp.ClientSession,):
        """
        :param id_: an int or str
        :param url: a string, the unformatted url (missing parameters)
        :param session: a HTTP session
        :return: a dict, JSON representation of response.
        """
        target_url = url.format(id_)
        try:
            response = await session.request(method="GET", url=target_url)
            json_dict = await response.json()
        except aiohttp.ContentTypeError:
            return None
        else:
            return json_dict

    @classmethod
    async def process_requests(cls, mode: str, ids: list) -> tuple:
        """
        :param mode: a str
        :param ids: a list of int or str
        :return: list of dict, collection of response data from the endpoint.
        """
        url = "https://pokeapi.co/api/v2/%s/{}/" % mode
        async with aiohttp.ClientSession() as session:
            async_coroutines = [cls.get_pokedex_data(id_, url, session)
                                for id_ in ids]
            responses = await asyncio.gather(*async_coroutines)
            return responses
