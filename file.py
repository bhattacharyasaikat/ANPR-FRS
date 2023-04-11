import pandas as pd
data ={'Owner Name' :["saikat","ozear"],
      'Model Number':["yhyh","bullet"],
      'Registration Validity':[2025,2029],
      'PUC':["10-09-2030","2-3-24"],
      'Insurance':["10-09-2030","2-3-21"]
      }
df = pd.DataFrame(data,columns=['Owner Name','Model Number','Registration Validity','PUC','Insurance'])


print("the df is",df)
df.to_csv("test.csv")