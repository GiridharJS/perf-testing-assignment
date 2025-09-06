# perf_api/locustfile.py

from locust import HttpUser, task, between

class PerfUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def user_activity(self):
        self.client.get("/reports/user-activity?user_id=1&start=2023-01-01&end=2025-01-01")
