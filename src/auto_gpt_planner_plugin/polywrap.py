from polywrap_client import PolywrapClient
from typing import cast

from pathlib import Path
from polywrap_client import PolywrapClient, ClientConfig
from polywrap_core import Uri, InvokerOptions, UriPackageOrWrapper, UriResolver
from polywrap_client_config_builder import PolywrapClientConfigBuilder
from polywrap_uri_resolvers import FsUriResolver,SimpleFileReader, StaticResolver, RecursiveResolver
from polywrap_uri_resolvers import UriResolverAggregator
from polywrap_http_plugin import http_plugin


import asyncio



ipfs_wrapper_path = Path("fs//Users/robertohenriquez/pycode/polywrap/hackathon/Auto-GPT/autogpt/auto_gpt_workspace/wrappers/ipfs-http-client")


resolver = RecursiveResolver(
        UriResolverAggregator(
            [
                cast(UriResolver, FsUriResolver(file_reader=SimpleFileReader())),
                cast(UriResolver, StaticResolver({Uri("wrap://ens/wraps.eth:http@1.1.0", ipfs_wrapper_path): http_plugin()})),
            ]
        )
    )
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

def polywrap_ipfs():
    uri = Uri.from_str(
        f'fs//Users/robertohenriquez/pycode/polywrap/hackathon/Auto-GPT/autogpt/auto_gpt_workspace/wrappers/ipfs-http-client/build'
    )


    result =  asyncio.run(client.invoke(
            InvokerOptions(
                uri=uri,
                method="cat",
                args={
                    "cid": "QmZ4d7KWCtH3xfWFwcdRXEkjZJdYNwonrCwUckGF1gRAH9",
                    "ipfsProvider": "https://ipfs.io",
                },
            )
        )
    )
    return result

def explore_wrappers():
    # Query Database of wrappers

    # Read Schema, documentation and functions

    # Save this information in the AutoGPT workspace
    return "polywrap is used"

def use_polywrap():
    return "polywrap is used"


