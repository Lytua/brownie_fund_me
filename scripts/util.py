from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-developments"]
LOCAL_DEVELOPMENT_ENV = ["development", "ganache-local"]
DECIMALS = 8
INITIALANSWER = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_DEVELOPMENT_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key_rinkeby"])


def deploy_mocks():
    print("Deploying Mocks...")
    if len(MockV3Aggregator) == 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(INITIALANSWER, "ether"), {"from": get_account()}
        )
    print("Mocks Deployed!")
