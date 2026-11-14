


from tools.tavily__tool import tavily_search

from tools.flight__tool import search_flights
from tools.backend import run_travel_agent

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user",
)

print("\nFINAL RESPONSE:\n")
if isinstance(response, dict) and "answer" in response:
    print(response["answer"])
else:
    print("Unexpected response format:")
    print(response) 
# res = tavily_search("Best hotels in India")
# print(res)

# res = search_flights("Plan a 7 days Japan trip from Bangladesh")
# print(res)