import aiohttp


async def run_in_session(converter, method, args):
    async with aiohttp.ClientSession() as session:
        converter.session = session
        return await getattr(converter, method)(*args)
