from polywrap_client import PolywrapClient
from typing import cast

from pathlib import Path
from polywrap_client import PolywrapClient, ClientConfig
from polywrap_core import Uri, InvokerOptions, UriPackageOrWrapper
from polywrap_client_config_builder import PolywrapClientConfigBuilder
from polywrap_uri_resolvers import FsUriResolver,SimpleFileReader, StaticResolver, RecursiveResolver
from polywrap_uri_resolvers import UriResolverAggregator


import asyncio


BIGNUMBER_URI = Uri.from_str("wrap://ens/bignumber.wraps.eth")
BIGNUMBER_WRAPPER = Uri.from_str("wrap://fs/./wrappers/big-number")


resolver = FsUriResolver(SimpleFileReader())

config = ClientConfig(resolver=resolver)
client = PolywrapClient(config)



def polywrap_bignumber():
    

    uri = Uri.from_str(
        f'fs//Users/robertohenriquez/pycode/cloud/AGI/Auto-GPT/autogpt/auto_gpt_workspace/wrappers/bignumber'
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
    result = asyncio.run(client.invoke(options))
    return f"the result is {result}"


def explore_wrappers():
    # Query Database of wrappers

    # Read Schema, documentation and functions

    # Save this information in the AutoGPT workspace
    return "polywrap is used"



