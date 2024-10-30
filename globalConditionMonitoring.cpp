#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>

struct Region {
    std::string name;
    double temperature; // In Celsius
    double humidity; // In Percentage
    double airQuality; // AQI - Air Quality Index
};

class GlobalMonitor {
public:
    GlobalMonitor() {
        // Seed for random data simulation
        srand(static_cast<unsigned int>(time(nullptr)));

        // Initialize with some sample regions
        regions.push_back({"North America", randomTemperature(), randomHumidity(), randomAirQuality()});
        regions.push_back({"Europe", randomTemperature(), randomHumidity(), randomAirQuality()});
        regions.push_back({"Asia", randomTemperature(), randomHumidity(), randomAirQuality()});
        regions.push_back({"Africa", randomTemperature(), randomHumidity(), randomAirQuality()});
        regions.push_back({"South America", randomTemperature(), randomHumidity(), randomAirQuality()});
    }

    void updateConditions() {
        for (auto &region : regions) {
            region.temperature = randomTemperature();
            region.humidity = randomHumidity();
            region.airQuality = randomAirQuality();

            checkAnomalies(region);
        }
    }

    void displayConditions() const {
        std::cout << "Global Environmental Conditions:\n";
        for (const auto &region : regions) {
            std::cout << "Region: " << region.name << "\n";
            std::cout << " Temperature: " << region.temperature << " °C\n";
            std::cout << " Humidity: " << region.humidity << " %\n";
            std::cout << " Air Quality Index (AQI): " << region.airQuality << "\n\n";
        }
    }

private:
    std::vector<Region> regions;

    double randomTemperature() {
        return (rand() % 401 - 100) / 10.0; // Generates temperature between -10.0 and 30.0°C
    }

    double randomHumidity() {
        return rand() % 101; // Generates humidity between 0% and 100%
    }

    double randomAirQuality() {
        return rand() % 301; // Generates AQI between 0 and 300
    }

    void checkAnomalies(const Region &region) const {
        if (region.temperature > 35) {
            std::cout << "Warning: High temperature in " << region.name << "!\n";
        }
        if (region.humidity < 20) {
            std::cout << "Warning: Low humidity in " << region.name << "!\n";
        }
        if (region.airQuality > 150) {
            std::cout << "Warning: Poor air quality in " << region.name << "!\n";
        }
    }
};

int main() {
    GlobalMonitor monitor;

    // Simulating monitoring in a loop (update every 5 seconds for demonstration)
    for (int i = 0; i < 5; ++i) {
        std::cout << "Monitoring Update #" << i + 1 << ":\n";
        monitor.updateConditions();
        monitor.displayConditions();

        // Wait for 5 seconds
        std::this_thread::sleep_for(std::chrono::seconds(5));
    }

    return 0;
}
