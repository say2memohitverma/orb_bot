import oandapyV20
import oandapyV20.endpoints.transactions as trans
import oandapyV20.endpoints.orders as orders


class TradeClient:
    def __init__(self, accountID, token):
        self.__accountID = accountID
        self.__token = token
        self.__clientAPI = oandapyV20.API(access_token=token)

    def get_accountID(self):
        return self.__accountID

    def get_token(self):
        return self.__token

    def get_clientAPI(self):
        return self.__clientAPI

    def get_transaction_details(self, transactionID):
        """
        returns details of a transactionID
        """
        r = trans.TransactionDetails(accountID=self.__accountID, transactionID=transactionID)
        self.__clientAPI.request(r)
        return r.response

    def create_order(self, data):
        """
        Creates and executes order using clientAPI
        """
        order_obj = orders.OrderCreate(self.__accountID, data=data)
        resp = self.__clientAPI.request(order_obj)
        return (resp)