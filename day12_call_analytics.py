call_logs = ["Pankaj", "Ankit", "Pankaj", "Neha", "Ankit", "Ankit"]
call_count = {}

for name in call_logs:
    call_count[name] = call_count.get(name, 0) + 1

busy_agents = {}

for name, count in call_count.items():
    if count > 1:
        busy_agents[name] = count

print(call_count)
print(busy_agents)

target_agent = []

for name, count in call_count.items():
    if count == 2:
        target_agent.append(name)

print(target_agent)
