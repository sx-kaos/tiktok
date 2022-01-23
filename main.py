import os
import time
import asyncio
from os import system
from typing import List

import aiohttp

class c:
    grey = '\033[1;30;40m'
    red = '\033[1;31;40m'
    dark_red = '\033[2;31;40m'
    green  = '\033[1;32;40m'
    yellow  = '\033[1;33;40m'
    blue = '\033[1;34;40m'
    magenta = '\033[1;35;40m'
    cyan = '\033[1;36;40m'
    white = '\033[1;37;40m'



def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')


class Checker:
    def __init__(self, usernames: List[str]):
        self.to_check = usernames

    async def _check(self, session: aiohttp.ClientSession, username: str) -> None:
        async with session.head(f'https://www.tiktok.com/@{username}') as response:
            if response.status == 200:
                print(f'{c.red}[-] https://www.tiktok.com/@{username}')
            else:
                print(
                    '%s[+] https://www.tiktok.com/@%s%s'
                    % ('\u001b[32;1m', username, '\u001b[0m')
                )
                write_file(username)

    async def start(self):
        print('Loading, please hang on')
        async with aiohttp.ClientSession() as sess:
            return await asyncio.gather(*[self._check(sess, u) for u in self.to_check])


if __name__ == '__main__':
    system('cls && title username checker made by kaos [https://dsc.gg/kaos]')

    try:
        with open('usernames.txt', encoding='UTF-8') as f:
            username_list = [line.strip() for line in f]
    except FileNotFoundError:
        print("Please make a file called 'usernames.txt' and put the usernames you wanna check in there")
        input()

    checker = Checker(username_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checker.start())
    print("Press enter to exit")
    input()
