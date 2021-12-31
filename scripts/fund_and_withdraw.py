from brownie import FundMe
from scripts.util import *


def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entranceFee = fund_me.getEntranceFee()
    print(f"The entrance fee is: {entranceFee}")
    fund_me.fund({"from": account, "value": entranceFee})


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
