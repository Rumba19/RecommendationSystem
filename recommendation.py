import heapq

class RecommendationHeap:
    def __init__(self):
        self.recommendations = []

    def add_recommendation(self, score, item):
        heapq.heappush(self.recommendations, (score, item))

    def get_top_k(self, k):
        return heapq.nlargest(k, self.recommendations)

# construct recommendation heap to get the top rank item 
# recommendation_heap = RecommendationHeap()
# recommendation_heap.add_recommendation(0.90, "item1")
# recommendation_heap.add_recommendation(0.60, "item2")
# recommendation_heap.add_recommendation(0.92, "item3")
# recommendation_heap.add_recommendation(0.80, "item4")
# recommendation_heap.add_recommendation(0.60, "item5")
# recommendation_heap.add_recommendation(0.70, "item6")
# print(recommendation_heap.get_top_k(2))