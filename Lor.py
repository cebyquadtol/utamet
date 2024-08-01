from sklearn.model_selection import train_test_split

# Splitting the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, stratify=y)
