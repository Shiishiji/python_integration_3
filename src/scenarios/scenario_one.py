class ScenarioOneData:
    def __init__(self, manufacturer: str, screen_size: str, screen_type: str):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.screen_type = screen_type

    def is_valid(self) -> bool:
        """
        Validate if the class attributes are valid.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Check if all attributes are strings and not None, with a minimum length of 1
        return all(isinstance(attr, str) and attr is not None and len(attr) >= 1
                   for attr in [self.manufacturer, self.screen_size, self.screen_type])


def run_scenario_one(_data: ScenarioOneData):
    print("tests fired")

