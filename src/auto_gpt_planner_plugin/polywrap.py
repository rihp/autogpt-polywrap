from polywrap_client import PolywrapClient

from pathlib import Path
from polywrap_client import PolywrapClient, ClientConfig
from polywrap_core import Uri, InvokerOptions, UriPackageOrWrapper
from polywrap_client_config_builder import PolywrapClientConfigBuilder
from polywrap_uri_resolvers import RecursiveResolver, StaticResolver, ExtendableUriResolver

import asyncio



config = (
        PolywrapClientConfigBuilder()
        .add_env(Uri.from_str("ens/hello.eth"), {"hello": "world"})
        .build()
    )



client = PolywrapClient(config)

async def polywrap_bignumber():
    uri = Uri.from_str(
        f'fs/{Path(__file__).parent.joinpath("cases", "big-number").absolute()}'
    )
    args = {
        "arg1": "123",  # The base number
        "obj": {
            "prop1": "1000",  # multiply the base number by this factor
        },
    }
    options: InvokerOptions[UriPackageOrWrapper] = InvokerOptions(
        uri=uri, method="method", args=args, encode_result=False
    )
    result = await client.invoke(options)
    return f"the result is {result}"


def use_polywrap():
    
    return "polywrap is used"

asyncio.run(polywrap_bignumber())
