from brownie import FundMe, accounts, config, MockV3Aggregator, network
from scripts.util import *
from web3 import Web3


def deploy_fundMe():
    account = get_account()
    price_feed_address = get_price_feed_address()
    fundMe = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fundMe.address}")
    return fundMe


def get_price_feed_address():
    if network.show_active() not in LOCAL_DEVELOPMENT_ENV:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        return MockV3Aggregator[-1]


def main():
    deploy_fundMe()
