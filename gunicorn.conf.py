import os

workers = 2 * os.cpu_count() + 1

worker_class = 'sync'

workers_connections = 1000

bind = "0.0.0.0:8000"

threads = 10

max_requests = 1000
max_requests_jitter = 50

preload_app = True

timeout = 30