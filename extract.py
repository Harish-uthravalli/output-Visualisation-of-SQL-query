import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host="localhost", database = 'test',user="root", passwd="harishpro",use_pure=True)
    query = 'select c.ID as "Customer ID", c.CustomerName, p.Product ,o.No_of_units, s.value, (o.No_of_units *s.value) as Total from customer c , salesorders s, orderedunits o, products p where c.ID = s.customer_id and s.ID =o.order_id and p.ID = o.unit_id and p.Product IN ("Eletric Motor","Tyre");'
    result_dataFrame = pd.read_sql(query,mydb)
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))

#print(result_dataFrame.drop(['ID','No_of_units','value'],axis=1))
print(result_dataFrame)
import plotly.express as px
df = result_dataFrame.drop(['Customer ID','No_of_units','value'],axis=1)
fig = px.bar(df, x="CustomerName", y="Total")
fig.show()
