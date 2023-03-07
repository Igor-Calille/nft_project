#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT
from scripts.upload_to_pinata import pinata_upload


## 0-PUCSP-CONSOLACAO
#sample_token_uri = "ipfs://QmQAnMF6z2mShGJEE9naXKtJimNYHMYkptxebQYpwTQJSy"

## 1-PUCSP-PERDIZES
#sample_token_uri = "ipfs://Qmen2SM3bNkrvRVt63RSpFWDeqBZ8qpez7KymhntXP913w"


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    token_id = simple_collectible.tokenCounter()
    transaction = simple_collectible.createCollectible(pinata_upload(), {"from": dev})
    transaction.wait(1)
    print(
        "Postagem realizada! Agora voce pode ver sua nft em {}".format(
            OPENSEA_FORMAT.format(simple_collectible.address, token_id)
        )
    )
    print('Porfavor, espere por ate 10 minutos para a postagem da nft e clique no botao de recarregar a pagina')


