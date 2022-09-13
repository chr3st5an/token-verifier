"""
TokenVerifier
~~~~~~~~~~~~~

Fast and simple script for checking the validity of discord
user tokens.

This script utilizes an asynchronous programming style
for fast token validation and lightweight execution. In
order to achieve this, `aiohttp` & `Brotli` are required
along with `colorama` for colored output.

This script is licensed under the MIT license.

Found a bug? => https://github.com/chr3st5an/token_verfier
"""

from typing import Any, Callable, Coroutine, Dict, Set, Union
from string import ascii_letters, ascii_lowercase, digits
from functools import wraps
from time import monotonic
from random import choices
import asyncio
import json
import os

# 3rd party packages
from aiohttp import ClientSession, DummyCookieJar
from colorama import Fore


# metadata
__author__  = "chr3st5an"
__version__ = "1.0.0"
__license__ = "MIT"


# constants
ALPHANUMERIC = ascii_letters + digits
ENDPOINT     = "https://discord.com/api/v9/users/@me/relationships"


def randstr(length: int, /, population: str = ALPHANUMERIC) -> str:
    """Generate a random string

    Parameters
    ----------
    length : str
        The desired string length
    population : str, optional
        The charset that gets used to generate the
        string, by default alphanumeric characters
        are used
    """

    return "".join(choices(population, k=length))


def load_tokens(path: Union[os.PathLike, str]) -> Set[str]:
    """Load the tokens from the given file
    """

    try:
        with open(path) as file:
            return {line.strip() for line in file if line.strip()}
    except Exception:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Couldn't load tokens from specified file")

    return set()


def stopwatch(coroutinefunction: Callable[..., Coroutine[None, None, Any]], /):
    """|decorator|

    Print the amount of time that the given
    coroutinefunction took to execute
    """

    @wraps(coroutinefunction)
    async def wrapper(*args, **kwargs) -> Any:
        start  = monotonic()
        result = await coroutinefunction(*args, **kwargs)

        print(f"{Fore.GREEN}|\n|\n{round(monotonic() - start, 2)}s{Fore.RESET}")

        return result

    return wrapper


async def verify_token(session: ClientSession, /, token: str) -> None:
    """Verify if the given token belongs to a discord user

    Send a request to the discord servers and evaluate
    the response.

    Parameters
    ----------
    session : aiohttp.ClientSession
        The session with which the request gets made
    token : str
        The token to verify
    """

    headers = dict(session.headers)
    headers["authorization"] = token
    headers["x-super-properties"] = randstr(380)

    cookies = {
        "__cfuid"  : randstr(43, ascii_lowercase + digits),
        "__dcfduid": randstr(32, ascii_lowercase + digits),
    }

    async with session.get(ENDPOINT, cookies=cookies, headers=headers) as response:
        if response.status in range(200, 205):
            return print(f"{Fore.GREEN}[+]{Fore.RESET} {token}")

        print(f"{Fore.RED}[-]{Fore.RESET} {token}")


@stopwatch
async def main() -> None:
    tokens = load_tokens(
        input(f"{Fore.LIGHTBLUE_EX}[FILE]{Fore.RESET} Tokens: ")
    )

    try:
        with open("./data/http_header.json") as file:
            headers: Dict[str, str] = json.load(file)
    except FileNotFoundError:
        headers = {}

    async with ClientSession(cookie_jar=DummyCookieJar(), headers=headers) as session:
        await asyncio.gather(*[
            verify_token(session, token) for token in tokens
        ])

    print(f"{Fore.GREEN}[FINISHED]{Fore.RESET}")


if __name__ == "__main__":
    asyncio.run(main())
