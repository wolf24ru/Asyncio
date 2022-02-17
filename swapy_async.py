import asyncio
import aiohttp
import time


async def get_person(person_id: int) -> dict:
    session = aiohttp.client.ClientSession()
    response = await session.get(f'https://swapi.dev/api/people/{person_id}')
    json_response = await response.json()
    await session.close()
    return json_response


async def main():
    get_person_corotins = []
    for person_id in range(1, 11):
        get_person_coro = get_person(person_id)
        get_person_corotins.append(get_person_coro)
    persons = await asyncio.gather(*get_person_corotins)
    print(persons)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'Время работы {time.time() - start}')
