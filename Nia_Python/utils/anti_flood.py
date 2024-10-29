import time
from collections import defaultdict

MESSAGE_LIMIT = 5
TIME_WINDOW = 10
message_times = defaultdict(list)

def check_flood(user_id):
    current_time = time.time()
    message_times[user_id] = [t for t in message_times[user_id] if current_time - t < TIME_WINDOW]
    if len(message_times[user_id]) >= MESSAGE_LIMIT:
        return True
    message_times[user_id].append(current_time)
    return False
