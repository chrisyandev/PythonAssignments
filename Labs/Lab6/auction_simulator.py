"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        """ Initializes the auctioneer state. """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders.clear()
        self._highest_bid = 0
        self._highest_bidder = None

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for b in self.bidders:
            if b is not self._highest_bidder:
                b(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bidder is None:
            self._highest_bid = bid
        elif bid > self._highest_bid:
            highest_bidder_name = "Starting bid" if \
                self._highest_bidder is None else self._highest_bidder.name
            print(f"{bidder.name} bidded {bid} in response to "
                  f"{highest_bidder_name}'s bid of {self._highest_bid}!")
            self._highest_bid = bid
            self._highest_bidder = bidder
        self._notify_bidders()

    def get_highest_bidder(self):
        """
        Gets the Bidder who made the highest bid.
        :return: a Bidder
        """
        return self._highest_bidder

    def get_highest_bid(self):
        """
        Gets the highest bid amount.
        :return: a float
        """
        return self._highest_bid


class Bidder:

    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        """
        :param name: a string
        :param budget: a float
        :param bid_probability: a float
        :param bid_increase_perc: a float
        """
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        """
        Makes this object callable.
        :param auctioneer: an Auctioneer
        :return: none
        """
        roll = random.random()
        if roll <= self.bid_probability:
            my_bid = auctioneer.get_highest_bid() * self.bid_increase_perc
            if my_bid <= self.budget:
                auctioneer.accept_bid(my_bid, self)
                self.highest_bid = my_bid

    def __str__(self):
        """
        Returns this bidder's name.
        :return: a string
        """
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.auctioneer = Auctioneer()
        for b in bidders:
            self.auctioneer.register_bidder(b)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at {start_price}")
        self.auctioneer.accept_bid(start_price, None)


def main():
    """ Drives the program. """

    # Hardcoding the bidders.
    bidders = [Bidder("Jojo", 3000, random.random(), 1.2),
               Bidder("Melissa", 7000, random.random(), 1.5),
               Bidder("Priya", 15000, random.random(), 1.1),
               Bidder("Kewei", 800, random.random(), 1.9),
               Bidder("Scott", 4000, random.random(), 2)]

    print("\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)
    print()
    print(f"The winner of the auction is: "
          f"{my_auction.auctioneer.get_highest_bidder()} "
          f"at ${my_auction.auctioneer.get_highest_bid()}")
    print()

    bidder_dict = {b.name: b.highest_bid for b in my_auction.auctioneer.bidders}
    print("Highest Bids Per Bidder")
    for key, value in bidder_dict.items():
        print(f"Bidder: {key}   Highest Bid: {value}")


if __name__ == '__main__':
    main()

