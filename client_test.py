import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
        {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      time = quote["timestamp"]
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = round(((bid_price + ask_price) / 2), 2)

      test_data = getDataPoint(quote)
      expect_data = (stock, time, bid_price, ask_price, price)
      self.assertEqual(test_data, expect_data, "Test calculate price false %s expect %s" % (
          test_data[4], price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      time = quote["timestamp"]
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = round(((bid_price + ask_price) / 2), 2)

      test_data = getDataPoint(quote)
      expect_data = (stock, time, bid_price, ask_price, price)
      self.assertEqual(test_data, expect_data, "Test Bid greater than Ask price false Bid: %s, Ask: %s" % (
          bid_price, ask_price))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ the assertion  ------------ """
    prices = {}
    for quote in quotes:
        stock, _, _, _, price = getDataPoint(quote)
        prices[stock] = price
        
    test_data = getRatio(prices["ABC"], prices["DEF"])
    expect_price = round((prices["ABC"] / prices["DEF"]), 2)
    self.assertEqual(test_data, expect_price, "Ratio is not calculation is failed")


if __name__ == '__main__':
    unittest.main()
