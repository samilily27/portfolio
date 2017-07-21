#import libraries needed
import pandas
import matplotlib.pyplot as pit

url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"


data = pandas.read_csv( url, sep="\t")

#print(data)

#print(data.columns)

#print(len(data))
#most rows

print (sum(data["quantity"]))

data.quantity.plot(style="pink")
pit.show()
#Index(['order_id', 'quantity', 'item_name', 'choice_description','item_price']s
#      dtype='object')
