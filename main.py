from ofxparse import OfxParser

def main(file_path):
    # Test the OfxParser
    with open(file_path, "rb") as file_handle:
        ofx_obj = OfxParser.parse(file_handle)
        print(ofx_obj)
        for account in ofx_obj.accounts:
            print(account.account_id, account.statement.start_date, account.statement.end_date)
            for transaction in account.statement.transactions:
                print(transaction.date, transaction.amount, transaction.payee)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ofxparse.py <path_to_ofx_file>")
    else:
        main(sys.argv[1])
