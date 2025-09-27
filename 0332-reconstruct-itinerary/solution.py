class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        adjList = defaultdict(list)
        for origin, destiny in tickets:
            heapq.heappush(adjList[origin], destiny)
        tickets = adjList

#[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#itinerary = ["SFO", "ATL", "SFO", "JFK", "ATL", "JFK"]
#tickets = {"JFK": [], "SFO": [], "ATL": []}
        def useTickets(airport):
            while tickets[airport]:
                useTickets(heapq.heappop(tickets[airport]))
            itinerary.append(airport)

        useTickets("JFK")
        return itinerary[::-1]
