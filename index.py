"""

from . import util
import json
from enum import Enum
from past.builtins import basestring

def get_block(block_id, api_code=None):
    """Get a single block based on a block hash.
    :param str block_id: block hash to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Block` class
    """

    resource = 'rawblock/' + block_id
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Block(json_response)


def get_tx(tx_id, api_code=None):
    """Get a single transaction based on a transaction hash.
    :param str tx_id: transaction hash to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Transaction` class
    """

    resource = 'rawtx/' + tx_id
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Transaction(json_response)


def get_block_height(height, api_code=None):
    """Get an array of blocks at the specified height.
    :param int height: block height to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an array of :class:`Block` objects
    """

    resource = 'block-height/{0}?format=json'.format(height)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return [Block(b) for b in json_response['blocks']]


def get_address(address, filter=None, limit=None, offset=None, api_code=None):
    """Get data for a single address including an address balance and list of relevant transactions.
