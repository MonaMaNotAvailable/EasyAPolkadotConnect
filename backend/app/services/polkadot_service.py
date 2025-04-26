from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException

# Initialize connection to Polkadot mainnet
substrate = SubstrateInterface(
    url="wss://rpc.polkadot.io"  # Polkadot mainnet node
)

def check_connection():
    """
    Check connection to Polkadot and print the chain name.
    """
    try:
        print("Connected to:", substrate.chain)  # Query the chain name
    except SubstrateRequestException as e:
        print(f"Error connecting to Polkadot: {e}")

def send_payment(from_wallet: str, to_wallet: str, amount: float):
    """
    Send payment from one wallet to another on the Polkadot network.
    
    :param from_wallet: The sender's wallet address (can be a keypair or private key).
    :param to_wallet: The recipient's wallet address.
    :param amount: The amount to send in DOT.
    :return: The transaction hash.
    """
    try:
        # Get sender's keypair from a mnemonic or private key (this is just for demo)
        sender_keypair = substrate.keypair_from_mnemonic(from_wallet)

        # Create the transfer call
        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={'dest': to_wallet, 'value': int(amount * 10**10)}  # Amount in Planck (1 DOT = 10^10 Planck)
        )

        # Sign and send the extrinsic
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=sender_keypair)
        receipt = substrate.submit_extrinsic(extrinsic)

        # Return the transaction hash
        return receipt['extrinsic_hash']
    
    except SubstrateRequestException as e:
        print(f"Error sending payment: {e}")
        return None

def refund_payment(from_wallet: str, to_wallet: str, amount: float):
    """
    Refund payment from one wallet to another on the Polkadot network.
    
    :param from_wallet: The sender's wallet address.
    :param to_wallet: The recipient's wallet address.
    :param amount: The amount to refund in DOT.
    :return: The transaction hash.
    """
    return send_payment(from_wallet, to_wallet, amount)

def get_balance(wallet_address: str):
    """
    Fetch the balance of a given wallet on Polkadot.

    :param wallet_address: The wallet address to query for balance.
    :return: The balance of the wallet.
    """
    try:
        # Query for balance of the given wallet address
        balance = substrate.query(
            module='System', storage_function='Account',
            params=[wallet_address]
        )
        free_balance = balance['data']['free']  # Available balance (Planck)
        return free_balance / 10**10  # Convert Planck to DOT

    except SubstrateRequestException as e:
        print(f"Error fetching balance: {e}")
        return None