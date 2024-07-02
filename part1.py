def format_flight_itineraries(itineraries):
    result = ""

    for i, itinerary in enumerate(itineraries):
        name, origin, destination = itinerary

        itenerary_r = f"Itinerary {i+1}: {name} - From {origin} to {destination}"

        result += itenerary_r + "\n "

    result = result.strip()

    return result

itineraries = [("Alice", "New York", "London"),("Bob", "Tokyo", "San Francisco")]
final_result = format_flight_itineraries(itineraries)
print(final_result)