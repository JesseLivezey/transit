import argparse, sys, os, time
from dbaccess import TransitDB
from data_source import NextBus

def main(db_file, service, route, stop):
    db = TransitDB(db_file)
    preds = NextBus(service, route, stop)
            
    print('Storing prediction data in ' + db_file + '...')
    while True:
        time.sleep(10)
        try:
            db.write_predictions(preds.fetch())
        except KeyboardInterupt:
            break
    print('Done writing predictions to file: ' + db_file + '. Goodbye!')

if __name__ == '__main__':

    db_file = args.db_file
    main(db_file)
