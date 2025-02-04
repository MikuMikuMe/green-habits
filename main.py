Creating a comprehensive Python program for a project like "Green-Habits" that focuses on tracking and reducing the personal carbon footprint can involve several components. Below, I'll outline a simple version of this application with features for tracking activities, calculating carbon emissions, and providing actionable suggestions. Note that this is a basic version and could be expanded with more detail depending on specific requirements.

```python
import json

class GreenHabits:
    def __init__(self):
        # Initializing user activities and suggestions
        self.user_activities = {}
        self.suggestions = [
            {"activity": "Drive less", "benefit": "Reduce transportation emissions"},
            {"activity": "Eat less meat", "benefit": "Reduce agricultural emissions"},
            {"activity": "Use energy-efficient appliances", "benefit": "Reduce home energy use"}
        ]
        self.carbon_factors = {
            "car_miles": 0.411,   # kg CO2 per mile
            "electricity_kwh": 0.233,  # kg CO2 per kWh
            "beef_kg": 27.0   # kg CO2 per kg of beef
        }

    def add_activity(self, activity, amount):
        """Adds an activity with the corresponding amount to the user's list."""
        try:
            if activity in self.carbon_factors:
                if activity in self.user_activities:
                    self.user_activities[activity] += amount
                else:
                    self.user_activities[activity] = amount
                print(f"Added {amount} units of {activity}.")
            else:
                print(f"Activity '{activity}' is not recognized. Please try a different one.")
        except Exception as e:
            print(f"Error adding activity: {e}")

    def calculate_footprint(self):
        """Calculates the total carbon footprint based on user activities."""
        try:
            total_emissions = 0.0
            for activity, amount in self.user_activities.items():
                factor = self.carbon_factors.get(activity, 0)
                emissions = factor * amount
                total_emissions += emissions
                print(f"{amount} units of {activity} contribute to {emissions:.2f} kg CO2.")
            print(f"Total carbon emissions: {total_emissions:.2f} kg CO2.")
            return total_emissions
        except Exception as e:
            print(f"Error calculating footprint: {e}")
            return None

    def get_suggestions(self):
        """Provides actionable suggestions to reduce carbon footprint."""
        print("Actionable suggestions to reduce carbon footprint:")
        try:
            for suggestion in self.suggestions:
                print(f"- {suggestion['activity']}: {suggestion['benefit']}")
        except Exception as e:
            print(f"Error retrieving suggestions: {e}")

    def save_data(self, filename="user_data.json"):
        """Saves user activities to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.user_activities, file)
            print("User data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename="user_data.json"):
        """Loads user activities from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.user_activities = json.load(file)
            print("User data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
        except Exception as e:
            print(f"Error loading data: {e}")

if __name__ == "__main__":
    app = GreenHabits()

    # Load previous data
    app.load_data()

    # Adding activities
    app.add_activity("car_miles", 100)
    app.add_activity("electricity_kwh", 50)
    app.add_activity("beef_kg", 2)

    # Calculate and display the carbon footprint
    app.calculate_footprint()

    # Get actionable suggestions
    app.get_suggestions()

    # Save data
    app.save_data()
```

### Key Features:

1. **Error Handling**: The program includes basic error handling for adding activities, calculating footprint, retrieving suggestions, and saving/loading data.
2. **Data Persistence**: Uses JSON to save and load user activities.
3. **Carbon Calculation**: Implements a simple calculation of carbon footprints for different activities, such as driving or electricity usage.
4. **Suggestions**: Provides basic suggestions for reducing carbon footprint.

This version of the program is expandable, and you can add more intricate logging, user authentication, a more comprehensive database of activities and emission factors, or even a user interface with libraries like Flask for web applications or Tkinter for desktop apps.