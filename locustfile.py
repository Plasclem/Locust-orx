"""Locust load test targeting orchestra.eu."""
from locust import HttpUser, task, between


class OrchestraUser(HttpUser):
    host = "https://www.orchestra.eu"
    wait_time = between(1, 5)

    @task(3)
    def load_homepage(self) -> None:
        """Load the orchestra.eu landing page."""
        self.client.get("/")

    @task(2)
    def browse_collections(self) -> None:
        """Browse the collections section of the site."""
        self.client.get("/fr-fr/collections")

    @task(1)
    def view_store_locator(self) -> None:
        """View the store locator page."""
        self.client.get("/fr-fr/magasins")
