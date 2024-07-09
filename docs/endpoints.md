# SimpleGraphs API Endpoints

## `/plot`

```text
POST https://api.simplegraphs.crimsontwilight.in/plot
```

### Request

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

### Response

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
