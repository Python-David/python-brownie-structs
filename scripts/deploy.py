from brownie import accounts, SimpleStruct


def main():
    deploy()


def deploy():
    account = accounts[0]
    simple_struct = SimpleStruct.deploy({"from": account})
    print(f"Deployed at {simple_struct.address}")

    # Call function with struct input

    simple_struct_input = [2, 3]
    tx = simple_struct.addSimple(simple_struct_input, {"from": account})
    tx.wait(1)

    complex_struct_input = ["Python-David", [2, 3], False]
    tx = simple_struct.addComplex(complex_struct_input, {"from": account})
    tx.wait(1)

    # View struct

    print(simple_struct.seeSimple())
    print(simple_struct.seeComplex())
