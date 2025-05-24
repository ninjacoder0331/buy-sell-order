# Flask API for Vercel Deployment

A simple Flask API application optimized for deployment on Vercel.

## Features

- ✅ Flask web framework
- ✅ CORS support for cross-origin requests
- ✅ Multiple API endpoints
- ✅ Error handling
- ✅ JSON responses
- ✅ Vercel deployment ready

## API Endpoints

### GET `/`
Welcome endpoint that returns basic API information.

### GET `/api/health`
Health check endpoint to verify API status.

### GET `/api/hello?name=YourName`
Greeting endpoint with optional name parameter.

### GET/POST `/api/data`
- **GET**: Returns sample data array
- **POST**: Accepts JSON data and echoes it back

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Test the API:**
   - Open http://localhost:5000 in your browser
   - Test endpoints using curl or Postman

## Deployment to Vercel

### Prerequisites
- [Vercel CLI](https://vercel.com/cli) installed
- Vercel account

### Deploy Steps

1. **Install Vercel CLI (if not already installed):**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel
   ```

4. **Follow the prompts:**
   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N** (for new project)
   - What's your project's name? **Enter your desired name**
   - In which directory is your code located? **./** 

### Environment Variables

If you need environment variables, create them in your Vercel dashboard or use:
```bash
vercel env add
```

## File Structure

```
trading-api-integration/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel configuration
└── README.md          # This file
```

## Sample API Calls

### Using curl

```bash
# Health check
curl https://your-app.vercel.app/api/health

# Hello with name
curl https://your-app.vercel.app/api/hello?name=John

# POST data
curl -X POST https://your-app.vercel.app/api/data \
  -H "Content-Type: application/json" \
  -d '{"key": "value", "message": "Hello from client"}'
```

### Using JavaScript/Fetch

```javascript
// GET request
fetch('https://your-app.vercel.app/api/hello?name=John')
  .then(response => response.json())
  .then(data => console.log(data));

// POST request
fetch('https://your-app.vercel.app/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    key: 'value',
    message: 'Hello from client'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are in `requirements.txt`
2. **CORS Issues**: CORS is already configured, but you can modify it in `app.py`
3. **Deployment Fails**: Check that `vercel.json` is properly configured

### Logs

View deployment logs:
```bash
vercel logs
```

## Next Steps

- Add authentication (JWT, OAuth)
- Connect to a database (PostgreSQL, MongoDB)
- Add input validation
- Implement rate limiting
- Add comprehensive testing
- Set up CI/CD pipeline

## License

MIT License 