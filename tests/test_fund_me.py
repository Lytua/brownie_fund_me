from scripts.fund_and_withdraw import fund, withdraw
from scripts.util import *
from scripts.deploy import deploy_fundMe
import pytest
from brownie import accounts, network, exceptions


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fundMe()
    entrancefee = fund_me.getEntranceFee() + 100
    tx1 = fund_me.fund({"from": account, "value": entrancefee})
    tx1.wait(1)
    balance = fund_me.addressToAmountFunded(account.address)
    assert balance == entrancefee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    balance = fund_me.addressToAmountFunded(account.address)
    assert balance == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_DEVELOPMENT_ENV:
        pytest.skip("Only for local testing.")

    fund_me = deploy_fundMe()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
