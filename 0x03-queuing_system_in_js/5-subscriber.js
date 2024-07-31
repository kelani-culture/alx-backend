import { createClient } from 'redis';

// Create a Redis client
const subscriber = createClient();

// Listen for the connect event to confirm connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the error event to handle connection errors
subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(`Received message: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
