import os
import requests as r
import urllib.parse
from farcaster import Warpcast
from dotenv import load_dotenv
import logging 

load_dotenv()
mnemonic = os.getenv('MNEMONIC')


search_casts_endpoint = "https://searchcaster.xyz/api/search?text="


def create_client(mnemonic=mnemonic):
    try: 
        client = Warpcast(mnemonic=mnemonic)
        if client.get_healthcheck():
            print("Client passed healthcheck")
            return client 
        else:
            print("Client failed healthcheck")
            return none
    except Exception as e:
        print(f"Error creating client {e}")



def search_casts(client, query, endpoint=search_casts_endpoint):
    encoded_query = urllib.parse.quote(query)
    url = search_casts_endpoint + encoded_query
    response = r.get(url)

    return response

def run():
    logging.info("Creating client...")
    client = create_client()
    casts = search_casts(client, "book")


if __name__ == "__main__":
    run()
        