class hardwareSet:
    def __init__(self):
        self.__capacity = 0  # total number of units
        self.__availability = 0  # units available to checkout
        self.__checkout_value = 0  # number of units that were checked out


    def initialize_capacity(self,qty):
        self.__capacity = qty
        self.__availability = self.__capacity

    def set_capacity(self,qty):
        self.__capacity = qty

    def get_availability(self):

        return self.__availability  # number of unused units

    def get_capacity(self):
        return self.__capacity


    def check_out(self,qty):

        if(qty > self.__availability):
            return -1
        # if quantity<0

        self.__checkout_value = self.__checkout_value + qty
        self.__availability = self.__availability - qty
        return 0

    def get_checkedout_qty(self):
        return self.__checkout_value

    def check_in(self,qty):
        self.__availability = self.__availability + qty
        self.__checkout_value = self.__checkout_value - qty


