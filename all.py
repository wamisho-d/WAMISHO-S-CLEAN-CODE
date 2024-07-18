class WeatherFetcher:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city,{})
    
class WeatherParser:
    @staticmethod
    def parse_weather_data(data):
        if not data:
                return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degree, {condition}, Humidity: {"humidity"}%"
    
class WeatherApp:
    def __init__(self):
          self.fetcher = WeatherFetcher()
          self.parser = WeatherParser()

    def get_detailed_forecast(self, city):
         data = self.fetcher.fetch_weather_data(city)
         return self.parser.parse_weather_data(data)
         

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if data:
             print(self.parser.parse_weather_data(data))
        else:
             print("Weather data not available")

app = WeatherApp()
app.display_weather("New York")
app.display_weather("London")
app.display_weather("Tokoyo")
app.display_weather("Paris")
             




               
        
        
        
