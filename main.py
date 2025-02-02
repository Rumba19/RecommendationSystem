from user_preferences import UserPreferences
from user_item_relation import RelationshipGraph
from user_product_activity import UserProductMatrix
from recommendation import RecommendationHeap
# Initialize components
user_preferences = UserPreferences()
interaction_graph = RelationshipGraph()
user_product_matrix = UserProductMatrix(2, 3)
recommendation_heap = RecommendationHeap()

# Demonstrate Hash Table
print("=== Hash Table (User Preferences) ===")
user_preferences.add_preferences("user1", "item1", 4)
user_preferences.add_preferences("user1", "item2", 2)
user_preferences.add_preferences("user2", "item1", 5)
print("User1 Preferences:", user_preferences.get_preferences("user1"))
print("User2 Preferences:", user_preferences.get_preferences("user2"))

# Demonstrate Graph
print("\n=== Graph (User-Item Interactions) ===")
interaction_graph.add_interaction("user1", "item1")
interaction_graph.add_interaction("user1", "item2")
interaction_graph.add_interaction("user2", "item1")
print("DFS Traversal from User1:", interaction_graph.dfs("user1"))

# Demonstrate Sparse Matrix
print("\n=== Sparse Matrix (User-Product Interactions) ===")
user_product_matrix.add_activity(0, 0, 5)  # User 0, Product 0, Rating 5
user_product_matrix.add_activity(0, 1, 3)  # User 0, Product 1, Rating 3
user_product_matrix.add_activity(1, 2, 2)  # User 1, Product 2, Rating 2
similarity_matrix = user_product_matrix.compute_similarity()
print("User-Product Similarity Matrix:\n", similarity_matrix)


recommendation_heap = RecommendationHeap()
recommendation_heap.add_recommendation(0.90, "item1")
recommendation_heap.add_recommendation(0.60, "item2")
recommendation_heap.add_recommendation(0.92, "item3")
recommendation_heap.add_recommendation(0.80, "item4")
recommendation_heap.add_recommendation(0.60, "item5")
recommendation_heap.add_recommendation(0.70, "item6")
print(recommendation_heap.get_top_k(2))