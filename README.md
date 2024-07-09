# SimpleGraphs API

SimpleGraphs is a user-friendly API that allows you to generate graphs from CSV files or JSON data without the need to set up your own server. Simply send your data to our endpoint, and receive a beautifully rendered graph in return.

## Features

- Generate graphs from CSV files or JSON data
- Support for multiple data series in a single graph
- API key authentication for secure access
- Returns graphs as PNG images

## API Endpoint

The base URL for all API requests is:

```text
https://api.simplegraphs.crimsontwilight.in
```

API endpoints can be found in [API Reference](docs/endpoints.md).

## Authentication

All requests to the SimpleGraphs API require an API key. Currently, `TESTAPI` is the only valid API key and can be used for freely.

## Usage

### Generating a Graph

To generate a graph, send a POST request to the `/plot` endpoint.

#### Endpoint

```text
POST https://api.simplegraphs.crimsontwilight.in/plot
```

#### Request

You can send data in two formats:

1. CSV File Upload:
   - Content-Type: `multipart/form-data`
   - Body:
     - `file`: Your CSV file
     - `api_key`: Your API key

2. JSON Payload:
   - Content-Type: `application/json`
   - Body:

     ```json
     {
       "api_key": "Your API key",
       "data": [
         ["x_axis", "series1", "series2", ...],
         [x1, y1_1, y1_2, ...],
         [x2, y2_1, y2_2, ...],
         ...
       ]
     }
     ```

#### Response

- Content-Type: `image/png`
- Body: PNG image of the generated graph

### Examples

1. Using cURL with a CSV file:

```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/your/file.csv" -F "api_key=YOUR_API_KEY" https://api.simplegraphs.crimsontwilight.in/plot --output graph.png
```

1. Using cURL with JSON data:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"api_key": "YOUR_API_KEY", "data": [["Date", "Value1", "Value2"], ["2023-01-01", 10, 20], ["2023-01-02", 15, 25], ["2023-01-03", 12, 22]]}' https://api.simplegraphs.crimsontwilight.in/plot --output graph.png
```

1. Using Python with `requests` library:

```python
import requests

# For CSV file upload
files = {'file': open('path/to/your/file.csv', 'rb')}
data = {'api_key': 'YOUR_API_KEY'}
response = requests.post('https://api.simplegraphs.crimsontwilight.in/plot', files=files, data=data)

# For JSON payload
json_data = {
    'api_key': 'YOUR_API_KEY',
    'data': [
        ['Date', 'Value1', 'Value2'],
        ['2023-01-01', 10, 20],
        ['2023-01-02', 15, 25],
        ['2023-01-03', 12, 22]
    ]
}
response = requests.post('https://api.simplegraphs.crimsontwilight.in/plot', json=json_data)

# Save the graph
if response.status_code == 200:
    with open('graph.png', 'wb') as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code}, {response.text}")
```

## Error Handling

The API uses standard HTTP response codes to indicate the success or failure of requests. In case of an error, the response will include a JSON object with more details about the error.

## Rate Limiting

To ensure fair usage, API requests are subject to rate limiting.

## License

SimpleGraphs API is licensed under [GNU General Public License v3.0](LICENSE).
