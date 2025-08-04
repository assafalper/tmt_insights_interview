So you’re trying to add an item to the Inventory via the API but you're stuck getting the metadata part working correctly. 
No worries — let’s walk through exactly how to make this happen, step by step.


You want to create a new Inventory item using a POST request, and the metadata field should include these values:

* year (e.g. 1994)
* actors (e.g. list of names)
* imdb_rating (e.g. 8.8)
* rotten_tomatoes_rating (e.g. 91)
* film_locations (e.g. list of places or strings)


Here’s an example of what your JSON payload should look like when making a POST to /inventory/:
```
{
  "name": "Pulp Fiction",
  "language": 1,
  "type": 1,
  "metadata": {
    "year": 1994,
    "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
    "imdb_rating": 8.9,
    "rotten_tomatoes_rating": 92,
    "film_locations": ["Los Angeles", "Hollywood"]
  }
}
```

Make sure:

* language and type are valid existing IDs in your database.
* metadata must match the expected structure

You can test using curl like this:

```
curl -X POST http://localhost:8000/inventory/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Pulp Fiction",
    "language": 1,
    "type": 1,
    "metadata": {
      "year": 1994,
      "actors": ["John Travolta", "Uma Thurman"],
      "imdb_rating": 8.9,
      "rotten_tomatoes_rating": 92,
      "film_locations": ["Los Angeles"]
    }
  }'
```
