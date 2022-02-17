import requests
import time


def get_person(person_id: int) -> dict:
    return requests.get(f'https://swapi.dev/api/people/{person_id}').json()


def main():
    person_list = []
    for person_id in range(1, 11):
        person = get_person(person_id)
        person_list.append(person)
        print(person)
    print(person_list)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Время работы {time.time() - start}')