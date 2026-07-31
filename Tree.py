import csv
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 1. Load data - skip header manually
data = []
with open('data.csv', 'r') as f:
    lines = f.readlines()

for line in lines[1:]: # [1:] means skip first line = header
    line = line.strip().replace('"', '') # remove " and spaces
    if line == "": # skip empty lines
        continue
    parts = line.split(',')
    if len(parts) == 5:
        data.append({
            'Age': parts[0],
            'Experience': parts[1],
            'Rank': parts[2],
            'Nationality': parts[3],
            'Go': parts[4]
        })

print("Loaded rows:", len(data))

# 2. Convert to numbers
X = []
y = []
nat_map = {'UK': 0, 'USA': 1, 'N': 2}
go_map = {'YES': 1, 'NO': 0}

for row in data:
    X.append([int(row['Age']), int(row['Experience']), int(row['Rank']), nat_map[row['Nationality']]])
    y.append(go_map[row['Go']])

features = ['Age', 'Experience', 'Rank', 'Nationality']

# 3. Train model
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# 4. Plot and save
plt.figure(figsize=(12,8))
tree.plot_tree(dtree, feature_names=features, class_names=['NO','YES'], filled=True)
plt.savefig("tree.png")
print("Tree saved as tree.png")