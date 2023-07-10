import time
import json
import os

class LRUCache:
    def __init__(self, capacity, checkpoint_file, checkpoint_interval, ttl=None):
        self.cache = {}
        self.capacity = capacity
        self.access_times = {}
        self.checkpoint_file = checkpoint_file
        self.checkpoint_interval = checkpoint_interval
        self.ttl = ttl
        self.load_cache()

    def _evict(self):
        least_recently_used = min(self.access_times, key=self.access_times.get)
        del self.cache[least_recently_used]
        del self.access_times[least_recently_used]

    def get(self, key):
        if key in self.cache:
            self.access_times[key] = time.time()
            return self.cache[key]
        return None

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            self._evict()

        self.cache[key] = value
        self.access_times[key] = time.time()

    def load_cache(self):
        if os.path.exists(self.checkpoint_file):
            with open(self.checkpoint_file, 'r') as f:
                self.cache = json.load(f)

    def checkpoint(self):
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.cache, f)

    def purge_stale_entries(self):
        if self.ttl:
            current_time = time.time()
            stale_keys = [key for key, access_time in self.access_times.items() if current_time - access_time > self.ttl]
            for key in stale_keys:
                del self.cache[key]
                del self.access_times[key]

    def start_periodic_checkpoint(self):
        while True:
            time.sleep(self.checkpoint_interval)
            self.checkpoint()
            self.purge_stale_entries()