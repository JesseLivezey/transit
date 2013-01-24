import predictions
#Units tests for transit-stats
def main():
    predict = predictions.Prediction()
    predict.fetch_Prediction('actransit','18','0305120')
    for item in predict.get_Prediction():
        print item

if __name__ == '__main__':
    main()
