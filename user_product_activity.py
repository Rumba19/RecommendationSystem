from scipy.sparse import csr_matrix

class UserProductMatrix:
    def __init__(self, rows, cols):
        self.rows = []
        self.cols = []
        self.data = []
        self.shape = (rows, cols)

    def add_activity(self, user, item, rating):
        self.rows.append(user)
        self.cols.append(item)
        self.data.append(rating)

    def compute_similarity(self):
        matrix = csr_matrix((self.data, (self.rows, self.cols)), shape=self.shape)
        return matrix.dot(matrix.T).toarray()

# hardcoded data input
user_product_matrix = UserProductMatrix(2, 3)
user_product_matrix.add_activity(0, 0, 5)
user_product_matrix.add_activity(0, 1, 3)
user_product_matrix.add_activity(1, 2, 2)
print(user_product_matrix.compute_similarity())