import pandas as pd

data = [["Name", "Age", "Role"],
        ["Mayuri Subhash Mhatre", 28, "Marketing Business Analyst"],
        ["John Doe", 35, "Vendor Performance Analyst"],
        ["Jane Smith", 30, "Project Manager"]]

df = pd.DataFrame(data[1:], columns=data[0])
print(df)
