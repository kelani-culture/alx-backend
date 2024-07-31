import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Listen for the connect event to confirm connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the error event to handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
